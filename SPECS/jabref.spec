Name:           jabref3
Version:        3.7
Release:        1
Summary:        JabRef is a graphical Java application for editing BibTeX and Biblatex .bib databases.

Group:          Applications/Databases
License:        MIT License
URL:            http://www.jabref.org/
Source:         JabRef-%{version}.jar
Source1:        jabref.desktop
Source2:        jabref-app.png
Source3:        jabref3.startup.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-build
Obsoletes:      jabref

BuildArch:      noarch
#BuildRequires:  desktop-file-utils
Requires:       java >= 1.8.0

%description
JabRef is the true open source bibliography reference manager. It uses BibTeX as his native format. It is a wonderful editor of BibTeX files allowing you to perform several actions when dealing with such files. Just a couple of them: import BibTeXML, CSA, Refer or Endnote, ISI Web of Science, SilverPlatter, Medline or Pubmed (xml), Scifinder, JStor and RIS, OVID, INSPEC, Biblioscape, Sixpack. Export HTML, Docbook, BibTeXML, MODS, RTF, Refer or Endnote, OpenOffice.org, manage, search through BibTeX files. Program runs on Java and works with Microsoft Windows, Linux and Mac OS X operating systems.

%prep
%build


%install
#rm -rf $RPM_BUILD_ROOT
install -m 0755 -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 0755 -p %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/%{name}/JabRef-%{version}.jar

# install icon
install -m 0755 -d $RPM_BUILD_ROOT/usr/share/pixmaps
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT/usr/share/pixmaps/%{name}.png

# install executable
install -d $RPM_BUILD_ROOT%{_bindir}
install -m 0755 -p %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}
echo "java -jar %{_datadir}/\"%{name}/JabRef-%{version}.jar\" \"\$@\" & " >> $RPM_BUILD_ROOT%{_bindir}/%{name}

# install desktop file
install -m 0755 -d $RPM_BUILD_ROOT/%{_datadir}/applications
install -D -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_datadir}/applications/%{name}.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%dir %{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/JabRef-%{version}.jar
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Dec 1 2016 - <lars.vilhuber@cornell.edu>
- Added command line arguments to the script, which dropped them (thanks to a.peyser@fz-juelich.de)
* Sun Nov 29 2015 - <lars.vilhuber@cornell.edu>
- Updated to Version 3.0
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
