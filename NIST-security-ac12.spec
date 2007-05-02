Name: NIST-security-ac12
License: GPL
Group: System/Security
Summary: Implements AC-12 (NIST 800-53)
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1.0
Release: 1
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch
%define filename    %{name}.sh

%description
This implements control AC-12 Session Termination (NIST 800-53): 
"Security Control Requirement:
The information system automatically terminates a session after 20 minutes of inactivity."
It only logs out sessions at the console.

%prep

%build
cd %{buildroot}
echo '
if [[ ! -z $(tty 2>/dev/null | grep -E "/dev/tty?") ]]
then
 export TMOUT=1200        
fi
' > %{filename}

%install
cd %buildroot
install -d -m 755 -g root -o root %buildroot/etc/profile.d
install -m 755 -g root -o root %{filename} %buildroot/etc/profile.d/%{filename}
rm %{filename}

%clean

%files
/etc/profile.d/%{filename}

%changelog
* Wed May  2 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 1.0-1
- Made it slighty more general so it works on RH

* Tue May  1 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - 1.0-0
- Original version

