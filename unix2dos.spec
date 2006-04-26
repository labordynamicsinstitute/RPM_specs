#
# spec file for package unix2dos (Version 2.2)
#
# Copyright (c) 2005 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://www.suse.de/feedback/
#

# neededforbuild  

BuildRequires: aaa_base acl attr bash bind-utils bison bzip2 coreutils cpio cpp cracklib cvs cyrus-sasl db devs diffutils e2fsprogs file filesystem fillup findutils flex gawk gdbm-devel glibc glibc-devel glibc-locale gpm grep groff gzip info insserv less libacl libattr libgcc libselinux libstdc++ libxcrypt  m4 make man mktemp module-init-tools ncurses ncurses-devel net-tools netcfg openldap2-client openssl pam pam-modules patch permissions popt procinfo procps psmisc pwdutils rcs readline sed strace syslogd sysvinit tar tcpd texinfo timezone unzip util-linux vim zlib zlib-devel autoconf automake binutils gcc gdbm gettext libtool perl rpm

Name:         unix2dos
Summary:      UNIX to DOS text file format converter
Version:      2.2
Release:      226
License:      distributable, Other License(s), see package
Group:        Productivity/Text/Convertors
Source:       unix2dos-2.2.src.tar.gz
Patch0:       unix2dos-mkstemp.patch
Patch1:       unix2dos-2.2-segfault.patch
Patch2:       unix2dos-2.2-manpage.patch
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
%debug_package
%prep
%setup -q -c
%patch -p1 -b .sec
%patch1 -p1 -b .segf
%patch2 -p1 -b .man
perl -pi -e "s,^#endif.*,#endif,g;s,^#else.*,#else,g" *.[ch]

%description
Converts plain text files from UNIX format to DOS format.



Authors:
--------
    Benjamin Lin blin @ socs.uts.edu.au


%build
gcc $RPM_OPT_FLAGS -ounix2dos unix2dos.c

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -m755 unix2dos $RPM_BUILD_ROOT%{_bindir}
install -m444 unix2dos.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,0755)
%doc COPYRIGHT
%{_bindir}/unix2dos
%{_mandir}/*/*

%changelog -n unix2dos
* Mon Aug 12 2002 - bk@suse.de
- initial version 2.2
