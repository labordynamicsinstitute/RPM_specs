Name: sas-mkdefault
License: Commercial
Group: Application/Statistics
Summary: Make SAS the default
Packager: Lars Vilhuber
Version: 9.3.1
Release: 0
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
ln -s /opt/SAS_9.1.3/sas sas
%post


%preun

%postun

%clean

%files
%defattr(755,root,root)
/usr/local/bin/sas


%changelog
* Tue Oct  2 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 9-1
- Initial build

