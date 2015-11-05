Name: gui_password_reminder-SRD
License: None
Group: System
Summary: Little GUI reminder for expiring passwords
Packager: Lars Vilhuber <lars.vilhuber@cornell.edu>
Version: 1
Release: 3
Source0: password_expire.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: noarch


%description
In pure Linux GUI login environments, there is no native utility
to remind users of expiring passwords, and most environments don't
have a password-change utility that shows up when a password has expired 
(since in order to get the GUI, you need to be logged in). 

%prep

%build
#  extract the files
tar xzvf %{SOURCE0}

%install
# the actual application
install  -d -m 755 %buildroot/usr/bin
install  -d -m 755 %buildroot/opt/kde3/share/autostart
install  -p -m 755 password_expire.sh %buildroot/usr/bin
install  -p -m 755 password_expire.desktop  %buildroot/opt/kde3/share/autostart


#------------------------------------------------
# after uninstalling, clean up any leftover files
#------------------------------------------------
%postun

%clean


%files
%doc 
%attr(744,root,root) /opt/kde3/share/autostart/password_expire.desktop
%attr(755,root,root) /usr/bin/password_expire.sh

%changelog
* Fri Feb  6 2009 Lars Vilhuber <lars.vilhuber@cornell.edu> - 1-3
- Changed name to include SRD

* Tue Nov 25 2008 Lars Vilhuber <lars.vilhuber@cornell.edu> - 1-1
- Changed permissions on desktop file

* Mon Nov 24 2008 Lars Vilhuber <lars.vilhuber@cornell.edu> - 1-1
- Original version by Chad, minor adjustments by Lars

