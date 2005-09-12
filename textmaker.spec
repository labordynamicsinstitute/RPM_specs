Name: textmaker
License: Commercial
Group: Application/Office
Summary: Textmaker word processor
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2002
Release: 405
Source0: tml02.tgz
Source1: tml-extra.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386 

%description
There is only one word processor that is available for Windows, Linux, FreeBSD, Pocket PCs, Handheld PCs, Windows CE.NET, and now for Sharp Zaurus: TextMaker 2002.

A license is required for this software. To obtain a trial license, please go to http://www.softmaker.com/english/tmltrialreg_en.htm

%prep

%build

%install
cd %buildroot
# This puts the menu shortcuts in place
tar xzvf %{SOURCE1}  
# the actual application
mkdir -p -m 755 %buildroot/opt/softmaker
mkdir -p -m 755 %buildroot/usr/bin
cd %buildroot/opt/softmaker
tar xzvf %{SOURCE0}  


#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean
#rm -rf %buildroot/opt/softmaker/textmaker

%files
/opt/softmaker/textmaker/
/usr/bin/textmaker
/usr/share/applications/Textmaker.desktop