Name:           jabref-test
Version:        2.80dev
Release:        1
Summary:        JabRef project is a java application for bibtex databases

Group:          Applications/Databases
License:        GPL
URL:            http://jabref.sourceforge.net/
Source:         JabRef-2.80dev--snapshot--2015-10-30--master--8d8c744.jar
Source1:        %{name}.desktop
Source2:        %{name}.png
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-build

BuildArch:      noarch
#BuildRequires:  desktop-file-utils
Requires:       java >= 1.8.0

%description
JabRef is an open source bibliography reference manager. The native file format used by JabRef is BibTeX, the standard LaTeX bibliography format. JabRef runs on the Java VM (version 1.8 or newer), and should work equally well on Windows, Linux and Mac OS X.

%prep
%build


%install
#rm -rf $RPM_BUILD_ROOT
install -Dm 0755 -p %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/%{name}

# install icon
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/pixmaps
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT/usr/share/pixmaps/%{name}.png

# install executable
install -d $RPM_BUILD_ROOT%{_bindir}
echo "#!/bin/bash
java -jar %{_datadir}/"%{name} " & " > $RPM_BUILD_ROOT%{_bindir}/%{name}
chmod 755 $RPM_BUILD_ROOT%{_bindir}/%{name}

# install desktop file
install -m 0755 -d $RPM_BUILD_ROOT/%{_datadir}/applications
install -D -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_datadir}/applications/%{name}.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Feb 6 2012 - <lars.vilhuber@cornell.edu>
- version 2.7 Removed dependency on java-sun, seems to work fine with openjdk
* Mon Apr 26 2010 - <soes@gmx.net>
- update to version 2.6
* Tue Jun 23 2009 - <soes@gmx.net>
- update to version 2.5
* Fri Dec 12 2008 - <soes@gmx.net>
- version 2.4.2
- changed icon file location for compatibility with suse 11.1
* Tue Nov 2 2008 <soes@gmx.net>
- update to version 2.4.2
* Tue Oct 14 2008 <soes@gmx.net>
- update to version 2.4.1
- added translation to desktop file
* Wed Sep 4 2008 <soes@gmx.net>
- update to version 2.4
* Tue May 13 2008 <soes@gmx.net>
- cleaned changelog
