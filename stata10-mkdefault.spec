Name: stata10-mkdefault
License: Commercial
Group: Application/Statistics
Summary: Make Stata 10 the default
Packager: Lars Vilhuber
Version: 10
Release: 1
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Requires: stata10

%description
Creates links for Stata 10

%prep

%build

%install
# install the desktop stuff 
install -d %buildroot/usr/local/bin
cd %buildroot/usr/local/bin
ln -s stata10 stata
ln -s stata10-se stata-se
ln -s stata10-mp stata-mp
ln -s xstata10 xstata
ln -s xstata10-se xstata-se
ln -s xstata10-mp xstata-mp
%post


%preun

%postun

%clean

%files
%defattr(755,root,root)
/usr/local/bin/stata
/usr/local/bin/stata-se
/usr/local/bin/stata-mp
/usr/local/bin/xstata
/usr/local/bin/xstata-se
/usr/local/bin/xstata-mp


%changelog
* Tue Oct  2 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9-1
- Initial build

