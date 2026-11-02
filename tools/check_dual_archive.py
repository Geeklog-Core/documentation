#!/usr/bin/env python3
"""Verify the actual downloadable archive, not just staging files."""
from pathlib import Path
from html.parser import HTMLParser
import hashlib
import os
import zipfile

ROOT=Path(__file__).resolve().parents[1]
SOURCE=Path(os.environ["GEEKLOG_CORE_DOCS"]).resolve()
ARCHIVE=ROOT/"dist/geeklog-2.2.2-docs-preview.zip"
RECAPTCHA=Path(os.environ["GEEKLOG_RELEASE_RECAPTCHA_DOCS"])
EXPECTED_PREFIX="public_html/docs/"
class Anchors(HTMLParser):
    def __init__(self):
        super().__init__(); self.anchors=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        for key in ("id","name"):
            if a.get(key): self.anchors.add(a[key])
def anchors(content):
    p=Anchors();p.feed(content.decode("utf-8"));return p.anchors
def main():
    assert ARCHIVE.is_file(), "Archive missing"
    core={p.relative_to(SOURCE).as_posix():p for p in SOURCE.rglob("*") if p.is_file()}
    with zipfile.ZipFile(ARCHIVE) as z:
        names=z.namelist()
        assert len(names)==len(set(names)), "Duplicate ZIP entry"
        assert all(n.startswith(EXPECTED_PREFIX) and ".." not in Path(n).parts for n in names), "Unsafe path"
        zipped={n.removeprefix(EXPECTED_PREFIX) for n in names}
        recaptcha={p.relative_to(RECAPTCHA).as_posix():p for p in RECAPTCHA.rglob("*") if p.is_file()}
        for name,path in recaptcha.items():
            key="public_html/admin/plugins/recaptcha/docs/"+name
            assert key in names, f"Missing plugin-local documentation: {key}"
            assert hashlib.sha256(z.read(key)).digest()==hashlib.sha256(path.read_bytes()).digest(),f"Changed plugin document: {key}"
        assert zipped==set(core),f"Missing or added Core docs: {sorted(zipped ^ set(core))}"
        for name,path in core.items():
            actual=z.read(EXPECTED_PREFIX+name)
            if name!="english/install.html":
                assert hashlib.sha256(actual).digest()==hashlib.sha256(path.read_bytes()).digest(),f"Unexpected change: {name}"
        assert z.read(EXPECTED_PREFIX+"english/install.html")!=core["english/install.html"].read_bytes()
        original_install=anchors(core["english/install.html"].read_bytes())
        new_install=anchors(z.read(EXPECTED_PREFIX+"english/install.html"))
        assert original_install <= new_install, f"Missing install anchors: {original_install-new_install}"
        original_config=anchors(core["english/config.html"].read_bytes())
        packaged_config=anchors(z.read(EXPECTED_PREFIX+"english/config.html"))
        assert original_config==packaged_config
        assert "desc_site_url" in packaged_config,"Missing config help anchor"
        for plugin in ("calendar","links","polls","spamx","staticpages","xmlsitemap"):
            assert ("english/"+plugin+".html") in core, f"Missing Core plugin help: {plugin}"
            assert z.read(EXPECTED_PREFIX+"english/"+plugin+".html")==core["english/"+plugin+".html"].read_bytes()
        assert "english/config.html" in recaptcha, "Missing reCAPTCHA config help"
        assert b"../docstyle.css" in z.read(EXPECTED_PREFIX+"english/install.html")
        assert b"../images/logo.gif" in z.read(EXPECTED_PREFIX+"english/install.html")
        print(f"PASS: ZIP has {len(names)} files including {len(recaptcha)} reCAPTCHA docs, exactly one intentional Core overlay, historical install/config anchors and six other plugin help pages")
        print("NOTE: artifact is checked against pinned Core commit, not verified release ZIP")
if __name__=="__main__": main()
