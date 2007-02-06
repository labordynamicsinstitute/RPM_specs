Name: smartsvn
License: Commercial
Group: Development/Tools/Version Control
Summary: Multi-platform client for Subversionexternal link
URL    : http://smartcvs.com/smartsvn/index.html
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2.0.7
# adjust to match the version above
%define _version 2_0_7
Release: 0
Source0: smartsvn-generic-%{_version}.tar.gz
Source1: smartsvn-extra.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch
Requires: java >= 1.4.2


%description
SmartSVN is an innovative multi-platform client for Subversionexternal link, the designated successor of CVS. SmartSVN has powerful features like built-in File Compare/Merge, Change Report or Tag and Branch handling, which make your daily work with Subversion as easy as possible.

SmartSVN is the consequent successor of SmartCVS, which helps thousands of users to sail around the CVS cliffs. Don't settle with simple GUI wrappers around the command line executable. Try out the easy-of-use and intelligent features of SmartSVN, which works together with your Subversion server out of the box.

SmartSVN is available in two versions, a free Foundation version and the powerful Professional version.

%prep
%setup -n smartsvn-%{_version}

%build
# also extract the extras
tar xzvf %{SOURCE1}

%install
# the actual application
install  -d -m 755 %buildroot/opt/smartsvn/bin
install  -d -m 755 %buildroot/opt/smartsvn/lib
install  -p -m 755 -D bin/* %buildroot/opt/smartsvn/bin
install  -p -m 755 -D lib/* %buildroot/opt/smartsvn/lib
# the link
install  -d -m 755 %buildroot/usr/bin
ln -s ../../opt/smartsvn/bin/smartsvn.sh %buildroot/usr/bin/smartsvn
# get the menu entry right
install  -d -m 755 %buildroot/usr/share/applications
install  -p -m 755 smartsvn.desktop %buildroot/usr/share/applications/smartsvn.desktop
# now for the icons
install  -d -m 755 %buildroot/opt/smartsvn/lib/icons
install  -p -m 755 icon16.png %buildroot/opt/smartsvn/lib/icons/
install  -p -m 755 icon32.png %buildroot/opt/smartsvn/lib/icons/
install  -p -m 755 icon48.png %buildroot/opt/smartsvn/lib/icons/
install  -p -m 755 icon64.png %buildroot/opt/smartsvn/lib/icons/

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean


%files
%doc changelog.txt license.html smartsvn.pdf smartsvn.url
%attr(755,root,-) /opt/smartsvn
%attr(755,root,-) /usr/bin/smartsvn
%attr(755,root,-) /usr/share/applications/smartsvn.desktop

%changelog
* Thu Jul  6 2006 Lars Vilhuber <lars.vilhuber@cornell.edu> - 2.0.1-0
- Updated to 2.0.1

* Thu Jan 26 2006 vilhuber@lservices
- Updated to 1.1.5
- Fixed icon on desktop file
