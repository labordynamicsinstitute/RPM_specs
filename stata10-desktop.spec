Name: stata10-desktop
License: Commercial
Group: Application/Statistics
Summary: Stata 10 desktop integratoin
Packager: Lars Vilhuber
Version: 10
Release: 1
BuildArch: noarch
Source0: stata10-desktop.tgz
Source1: stata10-icons.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Requires: stata10

%description
Creates links and desktop icons for Stata 10

%prep

%build

%install
tar xzf %{SOURCE0}
# install the desktop stuff 
install -d %buildroot/opt/kde3/share/applications
install -d %buildroot/usr/local/stata10/icons
install Stata10.desktop %buildroot/opt/kde3/share/applications
install Stata10-SE.desktop %buildroot/opt/kde3/share/applications
install Stata10-MP.desktop %buildroot/opt/kde3/share/applications
cd %buildroot/usr/local/stata10/icons
tar xzf %{SOURCE1}

%post


%preun

%postun

%clean

%files
%defattr(755,root,root)
/opt/kde3/share/applications/Stata10.desktop
/opt/kde3/share/applications/Stata10-MP.desktop
/opt/kde3/share/applications/Stata10-SE.desktop
/usr/local/stata10/icons/16x16/stata3.png
/usr/local/stata10/icons/16x16/stata2.png
/usr/local/stata10/icons/16x16/stata.png
/usr/local/stata10/icons/32x32/stata3.png
/usr/local/stata10/icons/32x32/stata2.png
/usr/local/stata10/icons/32x32/stata.png
/usr/local/stata10/icons/48x48/stata3.png
/usr/local/stata10/icons/48x48/stata2.png
/usr/local/stata10/icons/48x48/stata.png


%changelog
* Thu Aug 30 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 10-1
- Modified for Stata 10

* Thu Aug  9 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9-1
- Initial build

