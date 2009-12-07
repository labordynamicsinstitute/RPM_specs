Name: vrdc-menus
License: GPL
Group: Applications/Statistical
Summary: Creates a Statistics submenu, and the structure in /usr/share/applications to store VRDC-specific apps
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1
Release: 0 
Source0: vrdc-menus.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch

%description
Creates a Statistics submenu, and the structure in /usr/share/applications to store VRDC-specific apps

%prep

%build

%install
install -d -m 755 %buildroot/etc/xdg/menus/applications-merged/
install -d -m 755 %buildroot/usr/share/applications/vrdc/
install -d -m 755 %buildroot/usr/share/desktop-directories/
cd %buildroot
tar xzvf %{SOURCE0}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%dir /etc/xdg/menus/applications-merged
%dir /usr/share/desktop-directories
%dir /usr/share/applications
/etc/xdg/menus/applications-merged/statistics.menu
/usr/share/desktop-directories/Statistics.directory
/usr/share/applications/vrdc/

%changelog
* Mon Dec  7 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 1-0
- Initial version
 
