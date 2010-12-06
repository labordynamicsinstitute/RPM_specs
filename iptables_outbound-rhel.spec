
Summary: Provides a modified IP tables rule with outgoing filtering
Name: iptables_outbound
Version: 1
Release: 1
License: GPL
Group: Productivity/Networking/Firewall
Source0: iptables_out.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:  iptables
BuildArch: noarch

%description
Provides a modified IP tables rule with outgoing filtering

%prep
mkdir iptables_out

%build
cd iptables_out
tar xvzf %{SOURCE0}

%install
cd iptables_out
%__install -m 755 -d  "%{buildroot}/etc/sysconfig"
%__install -m 755 -d  "%{buildroot}/etc/init.d"
%__install -m 755 "./etc/init.d/iptables_out" "%{buildroot}/etc/init.d/iptables_out"
%__install -m 600 "./etc/sysconfig/iptables_out" "%{buildroot}/etc/sysconfig/iptables_out"


%clean
rm -rf iptables_out
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
%config %attr(700,root,root) /etc/sysconfig/iptables_out
/etc/init.d/iptables_out

%changelog
* Mon Dec 6 2010 Lars Vilhuber <lars.vilhuber@cornell.edu> - iptables_out
- Initial build.

