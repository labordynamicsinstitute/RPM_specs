%define port 23

Summary: Adds a second instance of the SSHD server running on a different port
Name: sshd%port
Version: 1
Release: 1
License: GPL
Group: Productivity/Networking/SSH
Source0: sshd23-mods.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:  openssh-server
BuildArch: noarch

%description
Adds a second instance of the SSDH server.

%prep


%build
tar xzf %{SOURCE0}

%install
%__install -m 755 -d  "%{buildroot}/etc/ssh"
%__install -m 755 -d  "%{buildroot}/etc/init.d"
%__install -m 755 sshd23-rhel "%{buildroot}/etc/init.d/sshd%port"
%__install -m 755 sshd23_config "%{buildroot}/etc/ssh/sshd%{port}_config"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%config /etc/ssh/sshd%{port}_config
/etc/init.d/sshd%port

%changelog
* Wed Nov  3 2010 Lars Vilhuber <lars.vilhuber@cornell.edu> - sshd%port-1
- Initial build.

