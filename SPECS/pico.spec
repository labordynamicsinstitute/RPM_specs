Name: pico
License: U of Washington
Group: Productivity/Editors/Other
Summary: A small, easy to use editor
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 4.64
Release: 1
Source0: pico-bin.linux-rhe3.Z
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: ia64 

%description
Pico is a simple, display-oriented text editor based on the Pine message system composer. 
NOTE: this is a pre-compiled i386 binary, it should work on Itanium, but your mileage will vary.
%prep

%build

%install
cd %buildroot
# the actual application
mkdir -p -m 755 %buildroot/usr/bin
cd %buildroot/usr/bin
cp %{SOURCE0} .
uncompress pico-bin.linux-rhe3.Z
mv pico-bin.linux-rhe3 pico
chmod a+rx pico

#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean

%files
/usr/bin/pico
