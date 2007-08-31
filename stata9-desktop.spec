Name: stata9-desktop
License: Commercial
Group: Application/Statistics
Summary: Stata 9 desktop integratoin
Packager: Lars Vilhuber
Version: 9
Release: 1
BuildArch: noarch
Source0: stata-desktop.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 

%description
Creates links and desktop icons for Stata

%prep

%build

%install
# install the desktop stuff 
install -d %buildroot/opt/kde3/share/applications
install -d %buildroot/opt/kde3/share/icons
tar xf %{SOURCE0}
install Stata.desktop %buildroot/opt/kde3/share/applications
install stata32.png %buildroot/opt/kde3/share/icons
%post


%preun

%postun

%clean

%files
%defattr(755,root,root)
/opt/kde3/share/applications/Stata.desktop
/opt/kde3/share/icons/stata32.png

%changelog
* Thu Aug  9 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9-1
- Initial build

