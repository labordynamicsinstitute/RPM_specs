Name: bootsplash-theme-SuSE92 
License: GPL
Group: System/Boot
Summary: SuSE 9.2 Bootsplash Themes
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 3.0 
Release: 0 
Source: 
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386 

%description
This package contains all bootsplash themes for SuSE 9.2
%prep

%build

%install
cd %buildroot
tar xzvf %{SOURCE0}  

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean
#rm -rf %buildroot/usr/local/stata8

%files
