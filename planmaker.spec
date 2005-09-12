Name: planmaker
License: Commercial
Group: Application/Office
Summary: Planmaker spreadsheet
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 2004
Release: 279
Source0: pml04.tgz
Source1: pml-extra.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i386 

%description
Use PlanMaker on the operating system of your choice: PlanMaker offers the same feature set on all platforms. This application is so compact and efficient that it even provides all its features on mobile Pocket PCs and Handheld PCs -  and fits in a few MBytes of RAM!

A license is required for this software. To obtain a trial license, please go to http://www.softmaker.com/english/pmltrialreg_en.htm

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
#rm -rf %buildroot/opt/softmaker/planmaker

%files
/opt/softmaker/planmaker/
/usr/bin/planmaker
/usr/share/applications/Planmaker.desktop