Name: gallery-remote
License: GPL
Group: Productivity/Publishing
Summary: Gallery Remote is a client-side Java application that provides users with a rich front-end to Gallery. This application makes it easier to upload images to your Gallery
URL: http://gallery.menalto.com/wiki/Gallery_Remote
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1.5
Release: 0
Source0: http://superb.dl.sourceforge.net/sourceforge/gallery/GalleryRemote.%{Version}.Linux.NoVM.bin
Source1: jabref-extra.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch
Requires: java >= 1.4.2 ImageMagick jpeg


%description
JabRef is an open source bibliography reference manager. The native file format used by JabRef is BibTeX, the standard LaTeX bibliography format. JabRef runs on the Java VM (version 1.4.2 or greater), and should work equally well on Windows, Linux and Mac OS X.

BibTeX is an application and a bibliography file format written by Oren Patashnik and Leslie Lamport for the LaTeX document preparation system. General information about BibTeX.

Bibliographies generated by LaTeX and BibTeX from a BibTeX file can be formatted to suit any reference list specifications through the use of different BibTeX style files. We support this initiative to build a searchable database of BibTeX style files, organized by journal names: LaTeX bibliography style database.


%prep
[[ -d jabref ]] && rm -r jabref
mkdir jabref
cd jabref
cp %{SOURCE0} .
# also extract the extras
tar xzvf %{SOURCE1}

%build


%install
# the actual application
cd jabref
install -d -m 755 %buildroot/opt/jabref/
install -p -m 755  JabRef-%{version}.jar %buildroot/opt/jabref/Jabref.jar
install -p -m 755 -D *png %buildroot/opt/jabref
# the link
install -d -m 755 %buildroot/usr/local/bin
install -p -m 755 jabref %buildroot/usr/local/bin/
# get the menu entry right
install -d -m 755 %buildroot/usr/share/applications
install -p -m 755 jabref.desktop %buildroot/usr/share/applications/jabref.desktop

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean


%files
%doc 
/opt/Gallery_Remote/LICENSE
/opt/Gallery_Remote/README
/opt/Gallery_Remote/Documentation/pretty-html.css
/opt/Gallery_Remote/Documentation/index.html
/opt/Gallery_Remote/Documentation/images/up.gif
/opt/Gallery_Remote/Documentation/images/up-up.gif
/opt/Gallery_Remote/Documentation/images/basic-auth.gif
/opt/Gallery_Remote/Documentation/html.css
/opt/Gallery_Remote/Documentation/gallery-remote.using.html
/opt/Gallery_Remote/Documentation/gallery-remote.software.html
/opt/Gallery_Remote/Documentation/gallery-remote.protocol3.html
/opt/Gallery_Remote/Documentation/gallery-remote.protocol.html
/opt/Gallery_Remote/Documentation/gallery-remote.problems.html
/opt/Gallery_Remote/Documentation/gallery-remote.intro.html
/opt/Gallery_Remote/Documentation/gallery-remote.i18n.html
/opt/Gallery_Remote/Documentation/gallery-remote.html
/opt/Gallery_Remote/Documentation/gallery-remote.faq.html
/opt/Gallery_Remote/img/default.gif
/opt/Gallery_Remote/img/WebComponentAdd16.gif
/opt/Gallery_Remote/img/WebComponent16.gif
/opt/Gallery_Remote/img/Up16.gif
/opt/Gallery_Remote/img/Stop16.gif
/opt/Gallery_Remote/img/Save16.gif
/opt/Gallery_Remote/img/RotateRight24.gif
/opt/Gallery_Remote/img/RotateLeft24.gif
/opt/Gallery_Remote/img/Preferences16.gif
/opt/Gallery_Remote/img/Open16.gif
/opt/Gallery_Remote/img/New16.gif
/opt/Gallery_Remote/img/Information16.gif
/opt/Gallery_Remote/img/FlipHoriz24.gif
/opt/Gallery_Remote/img/Down16.gif
/opt/Gallery_Remote/img/Delete16.gif
/opt/Gallery_Remote/img/computer.gif
/opt/Gallery_Remote/img/Copy16.gif
/opt/Gallery_Remote/img/Cut16.gif
/opt/Gallery_Remote/img/Paste16.gif
/opt/Gallery_Remote/img/uploading.gif
/opt/Gallery_Remote/lib/metadata-extractor-2.1.jar
/opt/Gallery_Remote/jpegtran/linux/jpegtran
/opt/Gallery_Remote/jpegtran/jpegtran.properties
/opt/Gallery_Remote/imagemagick/im.properties
/opt/Gallery_Remote/imagemagick/HOWTO
/opt/Gallery_Remote/GalleryRemote.jar
/opt/Gallery_Remote/defaults.properties
/opt/Gallery_Remote/ChangeLog
/opt/Gallery_Remote/Gallery_Remote_Debug.lax
/opt/Gallery_Remote/Gallery_Remote_Debug
/opt/Gallery_Remote/Gallery_Remote.lax
/opt/Gallery_Remote/Gallery_Remote
/opt/Gallery_Remote/lax.jar
/opt/Gallery_Remote/UninstallerData/installvariables.properties
/opt/Gallery_Remote/UninstallerData/.com.zerog.registry.xml
/opt/Gallery_Remote/UninstallerData/InstallScript.iap_xml
/opt/Gallery_Remote/UninstallerData/Uninstall_gallery_remote.lax
/opt/Gallery_Remote/UninstallerData/Uninstall_gallery_remote
/opt/Gallery_Remote/UninstallerData/uninstaller.jar


%changelog
* Thu Jan 26 2006 vilhuber@lservices
- First jabref rpm
