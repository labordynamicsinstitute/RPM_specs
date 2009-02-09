Name: sas-mkdefault
License: Commercial
Group: Application/Statistics
Summary: Make SAS the default
Packager: Lars Vilhuber
Version: 9.2
Release: 1
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
Requires: sas

%description
Creates links for SAS

%prep

%build

%install
# install the desktop stuff 
install -d %buildroot/usr/local/bin
cd %buildroot/usr/local/bin
ln -s sas92 sas9
ln -s sas9 sas

%post


%preun

%postun

%clean

%files
%defattr(755,root,root)
/usr/local/bin/sas
/usr/local/bin/sas9


%changelog
* Mon Feb  9 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9.3.1-1
- Made the link relative to /usr/local/bin

* Tue Oct  2 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9-1
- Initial build

