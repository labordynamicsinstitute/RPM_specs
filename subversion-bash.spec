Summary: Provides completion for the Subversion svn command under bash
Name: subversion-bash
Version: 1
Release: 1
License: GPL
Group: System
BuildArch: noarch
URL: http://svn.collab.net/repos/svn/trunk/tools/client-side/bash_completion
Source0: svn_completion.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description

%prep


%build
tar xzvf %{SOURCE0}

%install
rm -rf $RPM_BUILD_ROOT
install -D -o root -g root svn_completion.sh %buildroot/etc/bash_completion.d/svn_completion.sh
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/bash_completion.d/svn_completion.sh


%changelog
* Tue Mar 13 2007 Lars Vilhuber <lars.vilhuber@cornell.edu> - bash-1
- Initial build.

