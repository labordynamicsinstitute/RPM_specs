Name: vrdc-menus
License: GPL
Group: Applications/Statistical
Summary: Creates a Statistics submenu, and the structure in /usr/share/applications to store VRDC-specific apps
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1
Release: 6
Source0: vrdc-menus.tgz
Source1: vrdc-menus-super.tgz
Source2: vrdc-menus-icons.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch: noarch

%description
Creates a Statistics submenu, and the structure in /usr/share/applications to store VRDC-specific apps

%prep

%build
# create it
# source for icons:
# http://bestclipartblog.com/clipart-pics/cloud-clip-art-1.png
# http://commons.wikimedia.org/wiki/File:Rlogo.png
tar czvf %{SOURCE0} /usr/share/applications/vrdc/{ioctave,iqsub,Matlab,R,RStudio,SAS,iStata}.desktop
tar czvf %{SOURCE2} /usr/share/icons/vrdc

%install
install -d -m 755 %buildroot/etc/xdg/menus/applications-merged/
install -d -m 755 %buildroot/usr/share/applications/vrdc/
install -d -m 755 %buildroot/usr/share/icons/vrdc/
install -d -m 755 %buildroot/usr/share/desktop-directories/
cd %buildroot
# use it
tar xzvf %{SOURCE0}
tar xzvf %{SOURCE1}
tar xzvf %{SOURCE2}

%clean
rm -rf %buildroot

%files
%defattr(644,root,root,755)
%dir /etc/xdg/menus/applications-merged
%dir /usr/share/desktop-directories
%dir /usr/share/applications
%dir /usr/share/icons
/etc/xdg/menus/applications-merged/statistics.menu
/usr/share/desktop-directories/Statistics.directory
/usr/share/applications/vrdc/ioctave.desktop
/usr/share/applications/vrdc/iqsub.desktop
/usr/share/applications/vrdc/iStata.desktop
/usr/share/applications/vrdc/SAS.desktop
/usr/share/applications/vrdc/Matlab.desktop
/usr/share/applications/vrdc/R.desktop
/usr/share/applications/vrdc/RStudio.desktop
/usr/share/icons/vrdc/
%changelog
* Mon Dec  7 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 1-0
- Initial version
 
