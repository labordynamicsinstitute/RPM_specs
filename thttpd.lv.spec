#
# spec file for package thttpd (Version 2.25b)
#
# Copyright (c) 2004 SUSE LINUX AG, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://www.suse.de/feedback/
#

BuildRequires: aaa_base acl attr bash bind-utils bison bzip2 coreutils cpio cpp cracklib cvs cyrus-sasl db devs diffutils e2fsprogs file filesystem fillup findutils flex gawk gdbm-devel glibc glibc-devel glibc-locale gpm grep groff gzip info insserv less libacl libattr libgcc libnscd libselinux libstdc++ libxcrypt libzio m4 make man mktemp module-init-tools ncurses ncurses-devel net-tools netcfg openldap2-client openssl pam pam-modules patch permissions popt procinfo procps psmisc pwdutils rcs readline sed strace syslogd sysvinit tar tcpd texinfo timezone unzip util-linux vim zlib zlib-devel autoconf automake binutils gcc gdbm gettext libtool perl rpm

Name:         thttpd
License:      Other License(s), see package, X11/MIT
Group:        Productivity/Networking/Web/Servers
Provides:     http_daemon 
PreReq:       %fillup_prereq %insserv_prereq permissions
Autoreqprov:  on
Version:      2.25b
Release:      27.lv
Source:       %{name}-%{version}.tar.bz2
Source1:      %{name}-SuSE.tar.bz2
Patch0:       %{name}-%{version}-configure.patch
Patch1:       %{name}-%{version}-dirs.patch
Patch2:       %{name}-%{version}-time_h.patch
Patch3:       %{name}-%{version}-newautoconf.patch  
Patch4:       %{name}-%{version}-sec.patch
URL:          http://www.acme.com/software/thttpd/
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
Summary:      Small and very simple webserver

%description
Thttpd is a very compact no-frills httpd serving daemon that can handle
very high loads.  While lacking many of the advanced features of Roxen
or Apache, thttpd operates without forking and is extremely efficient
in memory use.	Basic support for cgi scripts, authentication, and ssi
is provided for.  Advanced features include the ability to throttle
traffic.



Authors:
--------
    jef@acme.com

%define prefix   /usr
%define sysconfdir /etc
%define serverroot /srv/www
%prep
%setup -a 1
%patch0
%patch1
%patch2
%patch3
%patch4
for i in README.SuSE SuSE/etc/init.d/thttpd; do
sed "s @SRVROOT@ %{serverroot}/thttpd " $i >$i.new
mv $i.new $i
done
chmod 744 SuSE/etc/init.d/thttpd
%{suse_update_config}

%build
mv aclocal.m4 acinclude.m4
libtoolize --force
aclocal
autoconf
V_CCOPT="$RPM_OPT_FLAGS" \
./configure --mandir=%{_mandir} \
                --prefix=%{prefix} \
                --infodir=%{_infodir} \
                --sysconfdir=%{sysconfdir}
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin \
	   $RPM_BUILD_ROOT/usr/sbin \
           $RPM_BUILD_ROOT/%{_mandir}/man1 \
           $RPM_BUILD_ROOT/%{_mandir}/man8 \
           $RPM_BUILD_ROOT%{serverroot}/thttpd/users
make DESTDIR=$RPM_BUILD_ROOT/ install
cp -a SuSE/* $RPM_BUILD_ROOT
sed "s@THTTPD-RELEASE@%{version}@" \
     $RPM_BUILD_ROOT%{serverroot}/htdocs/index.html.template > \
     $RPM_BUILD_ROOT%{serverroot}/thttpd/index.html
rm -f $RPM_BUILD_ROOT%{serverroot}/htdocs/index.html.template
mv $RPM_BUILD_ROOT%{serverroot}/htdocs/cgi-bin $RPM_BUILD_ROOT%{serverroot}/thttpd/ 
mv $RPM_BUILD_ROOT%{serverroot}/htdocs/gif $RPM_BUILD_ROOT%{serverroot}/thttpd/ 

%post
%{fillup_and_insserv thttpd}
%run_permissions

%verifyscript
%verify_permissions -e /usr/bin/makeweb

%preun
%stop_on_removal thttpd

%postun
%restart_on_update thttpd
%{insserv_cleanup}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README README.SuSE config.h
%{serverroot}/thttpd/cgi-bin
%{serverroot}/thttpd/gif
%attr(775, root, www) %{serverroot}/thttpd/users
%config %{serverroot}/thttpd/index.html
%verify(not mode) %attr(2750, root, www) /usr/bin/makeweb
/usr/bin/htpasswd
/usr/sbin/*
/usr/share/man/*/*
%config /etc/init.d/thttpd

%changelog -n thttpd
* Wed Sep 14 2005 - lars@vilhuber.com
- moved serverroot to serverroot/thttpd
* Tue Feb 17 2004 - tcrhak@suse.cz
- update to version 2.25b
* Tue Jan 13 2004 - schwab@suse.de
- Fix use of aclocal.
* Wed Oct 29 2003 - tcrhak@suse.cz
- update to 2.24, includes a fix for a buffer overflow [bug #32734]
- fixed virtual hosting security hole [bug #32757]
- fixed permissions according to permissions.secure,
  added macros %%run_permissions and %%verify_permissions
* Mon Sep 01 2003 - tcrhak@suse.cz
- added macros %%stop_on_removal and %%restart_on_update [bug #29022]
* Thu Jun 05 2003 - ro@suse.de
- remove unpackaged files from buildroot
* Tue Mar 11 2003 - tcrhak@suse.cz
- fixed permissions of the init scipt [bug #25084]
* Tue Oct 15 2002 - tcrhak@suse.cz
- substitute correct servroot during built
* Mon Oct 14 2002 - tcrhak@suse.cz
- use /srv/www rather then /usr/local/httpd [bug #20802]
* Fri Aug 02 2002 - ro@suse.de
- adapt server root
* Sat Jul 27 2002 - kukuk@suse.de
- Change group from wwwadmin to www
* Sat Jul 27 2002 - adrian@suse.de
- do not source rc.config anymore
* Tue Jul 02 2002 - tcrhak@suse.cz
- update to version 2.23beta1
* Tue Jan 15 2002 - tcrhak@suse.cz
- update to version 2.20c
- added thttpd-2.20c-sec.patch
- removed START_THTTPD from README.SuSE
* Tue Jan 15 2002 - ro@suse.de
- removed START_THTTPD
* Fri Sep 21 2001 - bjacke@suse.de
- fix version on template webpage
* Mon Sep 03 2001 - adostal@suse.cz
- fix /etc/init.d in thttpd-SuSE.tar.bz2 files
- split patches on configure, dirs, time_h and newautoconf
* Thu Jun 14 2001 - adostal@suse.cz
- fix for new autoconf
* Fri Apr 13 2001 - nadvornik@suse.cz
- changed initscript according to skeleton
* Thu Mar 08 2001 - nadvornik@suse.cz
- compiled with RPM_OPT_FLAGS
* Thu Feb 15 2001 - nadvornik@suse.cz
- fixed to compile
* Wed Dec 13 2000 - smid@suse.cz
- generatig of default page moved to %%install (it was in %%post and
- caused [#4566]
* Tue Dec 12 2000 - smid@suse.cz
- default cgibin pattern changed [#4564]
- rcthttpd link added
* Sun Dec 03 2000 - smid@suse.cz
- new version: 2.20b
* Fri Dec 01 2000 - ro@suse.de
- moved init-script
* Thu Nov 02 2000 - smid@suse.cz
- fix ugly bug in startup scripts
* Thu Sep 28 2000 - smid@suse.cz
- new version: 2.20
* Wed Aug 30 2000 - smid@suse.cz
- fix bug in startup script
* Wed Jul 05 2000 - mha@suse.de
- new version: 2.19
* Tue May 23 2000 - smid@suse.cz
- buildroot fixed
* Wed May 03 2000 - smid@suse.cz
- buildroot added
* Tue Mar 21 2000 - mha@suse.de
- update to 2.16
* Fri Mar 03 2000 - uli@suse.de
- moved man pages to %%{_mandir}
* Mon Feb 28 2000 - mha@suse.de
- new version: 2.15
* Thu Feb 17 2000 - dipa@suse.de
- bug #1268 rc.config variable set to no
* Wed Jan 12 2000 - mha@suse.de
- new version: 2.11
- new conflicts (roxen, apache, aolserv), provides (http_daemon)
- new homepage
* Tue Nov 16 1999 - kukuk@suse.de
- Fix stack overflow
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Sep 09 1999 - bs@suse.de
- fixed call of Check at the end of %%install section
* Sun Jul 11 1999 - mha@suse.de
- new package: thttpd (a _small_ webserver)
  absolutely no configuration needed - and yet save (chroot)!
