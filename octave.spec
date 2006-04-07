#
# spec file for package octave (Version 2.1.71)
#
# Copyright (c) 2005 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://www.suse.de/feedback/
#

# norootforbuild
# neededforbuild  bison dejagnu expect flex g77 gmp gnuplot gperf gpp libgpp libpng readline-devel tcl termcap tetex

BuildRequires: aaa_base acl attr bash bind-utils bison bzip2 coreutils cpio cpp cracklib cvs cyrus-sasl db devs diffutils e2fsprogs file filesystem fillup findutils flex gawk gdbm-devel gettext-devel glibc glibc-devel glibc-locale gpm grep groff gzip info insserv syslogd less libacl libattr  libgcc  libselinux libstdc++ libxcrypt  m4 make man mktemp module-init-tools ncurses ncurses-devel net-tools netcfg openldap2-client openssl pam pam-modules patch permissions popt procinfo procps psmisc pwdutils rcs readline sed strace sysvinit tar tcpd texinfo timezone unzip util-linux vim zlib zlib-devel autoconf automake binutils dejagnu expect gcc gcc-c++ f2c gdbm gettext gmp gnuplot gperf libpng libstdc++-devel libtool perl readline-devel rpm tcl te_ams te_latex termcap tetex

Name:         octave
URL:          http://www.octave.org/
License:      GPL
Group:        Productivity/Scientific/Math
Provides:     matlab4 octave 
Requires:     gnuplot
PreReq:       %install_info_prereq
Autoreqprov:  on
Version:      2.1.71
Release:      2_sles9
Summary:      A high level programming language
Source:       %{name}-%{version}.tar.bz2
Patch:        octave-2.1.71.patch
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
%define       regenerate 1
%define       check	 	0

%description
Octave is a high level programming language. It's designed for the
solution of numeric problems. There is a command line interface
supplied. This version does not have FFTW or MPI enabled.



Authors:
--------
    John W. Eaton <jwe@bevo.che.wisc.edu>

%debug_package
%prep
%setup -q
%patch

%build
mkdir m4
mv aclocal.m4 m4/octave.m4
%{suse_update_config -f . scripts}
aclocal --force --verbose -I m4
#aclocal
autoconf -f --verbose
#autoreconf --force --verbose
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fno-strict-aliasing" \
CXXFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -fno-strict-aliasing" \
	./configure \
	--prefix=%{_prefix} \
	--exec-prefix=%{_prefix} \
	--libexecdir=%{_libdir} \
	--libdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--enable-shared \
	--enable-rpath \
	--disable-static \
	--enable-dl \
	--enable-lite-kernel
echo Building octave...
# regenerate info files
touch doc/conf.texi
make %{?jobs:-j%jobs}
%if %check
make check
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%_infodir 
install -d $RPM_BUILD_ROOT/%_mandir
make exec_prefix=$RPM_BUILD_ROOT/usr \
    libdir=$RPM_BUILD_ROOT/%_libdir \
    libexecdir=$RPM_BUILD_ROOT/%_libdir \
    prefix=$RPM_BUILD_ROOT/usr \
    mandir=$RPM_BUILD_ROOT/%_mandir \
    infodir=$RPM_BUILD_ROOT/%_infodir \
    install 
#install -m 644 doc/faq/*.info $RPM_BUILD_ROOT%{_infodir}
#install -m 644 doc/liboctave/*.info $RPM_BUILD_ROOT%{_infodir}
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
sed "s@$RPM_BUILD_ROOT@@g" < $RPM_BUILD_ROOT/%{_libdir}/octave/ls-R > xtmp
mv xtmp $RPM_BUILD_ROOT/%{_libdir}/octave/ls-R
sed "s@$RPM_BUILD_ROOT@@g" < $RPM_BUILD_ROOT/usr/share/octave/ls-R > xtmp
mv xtmp $RPM_BUILD_ROOT/usr/share/octave/ls-R

%clean
rm -rf $RPM_BUILD_ROOT

%post
%run_ldconfig
#%install_info --info-dir=%{_infodir} %{_infodir}/Octave-FAQ.info.gz
#%install_info --info-dir=%{_infodir} %{_infodir}/liboctave.info.gz
#%install_info --info-dir=%{_infodir} %{_infodir}/octave.info.gz

%postun
%run_ldconfig
#%install_info_delete --info-dir=%{_infodir} %{_infodir}/Octave-FAQ.info.gz
#%install_info_delete --info-dir=%{_infodir} %{_infodir}/liboctave.info.gz
#%install_info_delete --info-dir=%{_infodir} %{_infodir}/octave.info.gz

%files
%defattr(-,root,root)
%doc COPYING NEWS README THANKS PROJECTS doc/ChangeLog
%doc doc/faq/Octave-FAQ.{dvi,ps} doc/interpreter/octave.{dvi,ps}
%doc doc/liboctave/liboctave.{dvi,ps} doc/refcard/refcard-a4.{dvi,ps}
/usr/bin/*
%doc %{_infodir}/*.gz
%doc %{_mandir}/man1/*.gz
/usr/include/*
%_libdir/octave*
/usr/share/octave/

%changelog -n octave
* Tue Jun 28 2005 - anicka@suse.cz
- update to 2.1.71
* Wed May 11 2005 - ro@suse.de
- fix build with gcc4
* Mon Apr 18 2005 - mcihar@suse.de
- GNU Fortran 77 compiler now requires gmp, let's add it
- still doesn't compile, because GCC: TODO: Functions with alternate entry points
* Tue Dec 21 2004 - mcihar@suse.cz
- update to 2.1.64
- do not include info pages, as they are out of date
- string patching was not needed for long time, so drop the patch
* Thu Nov 11 2004 - ro@suse.de
- fixed file list
* Wed Aug 04 2004 - mcihar@suse.cz
- update to 2.1.57
* Fri Mar 05 2004 - mcihar@suse.cz
- really compile with -fno-strict-aliasing
- doesn't need f2c at all
* Fri Mar 05 2004 - mcihar@suse.cz
- update to 2.1.55
- fix info pages installation
- add some docs
- use -fno-strict-aliasing
* Fri Jan 09 2004 - adrian@suse.de
- add %%run_ldconfig
- use RPM_OPT_FLAGS
* Fri Aug 29 2003 - mcihar@suse.cz
- info pages should not be executable
* Wed Aug 13 2003 - ro@suse.de
- fix info page installation again (thanks to DJurzitza)
* Wed Jul 30 2003 - ro@suse.de
- install more info pages
* Thu Jun 26 2003 - ro@suse.de
- remove traces of buildroot from installed files
* Wed Jun 11 2003 - ltinkl@suse.cz
- updated sources to version 2.1.49
* Thu Apr 24 2003 - ro@suse.de
- fix install_info --delete call and move from preun to postun
* Mon Mar 03 2003 - ro@suse.de
- added info dir entries
* Tue Feb 25 2003 - mcihar@suse.cz
- removed -mminimal-toc as it is now part of RPM_OPT_FLAGS for ppc64
- added gnuplot to requires
* Mon Feb 10 2003 - mcihar@suse.cz
- used %%install_info macro (fixes bug #23443)
* Wed Feb 05 2003 - mcihar@suse.cz
- removed RPM_OPT_FLAGS="$RPM_OPT_FLAGS -mminimal-toc" for ppc64
  (fixes bug #23266)
- updated to 2.1.44
* Fri Nov 22 2002 - mcihar@suse.cz
- updated to 2.1.40, mostly only configure and automake fixes, it
  also fixes sstream and some other smaller issues with gcc 3.3
- fixed multiline string
* Tue Aug 06 2002 - mcihar@suse.cz
- updated to 2.1.36
* Sat Jun 29 2002 - olh@suse.de
- build with -mminimal-toc on ppc64, use RPM_OPT_FLAGS for CFLAGS
* Tue May 21 2002 - ro@suse.de
- call suse_update_config also for kpathsea subdir
* Wed May 08 2002 - ro@suse.de
- fix for latest gcc-snapshot
* Fri Apr 19 2002 - coolo@suse.de
- updating to octave 2.1.35 as octave 2.0.1[67] were hopeless
  with gcc 3.1 (gave up after 2 days of work)
* Tue May 08 2001 - mfabian@suse.de
- bzip2 sources
* Fri May 05 2000 - bubnikv@suse.cz
- added buildroot
- /usr/execlib/octave moved to /usr/lib/octave according to FHS 2.1
* Mon Feb 21 2000 - ro@suse.de
- update to 2.0.16
* Tue Jan 25 2000 - ro@suse.de
- update to 2.0.15
- man,info to /usr/share using macro
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Wed Jul 14 1999 - ro@suse.de
- update to 2.0.14
* Thu May 20 1999 - ro@suse.de
- use CFLAGS="-D_GNU_SOURCE"
* Mon Nov 23 1998 - ro@suse.de
- update to 2.0.13 / builds with glibc
* Wed Oct 07 1998 - ro@suse.de
- BETA: added f2c to neededforbuild
* Wed Jan 28 1998 - ro@suse.de
- removed libhistory.so & libreadline.so as well and link static
  to these
* Mon Nov 17 1997 - bs@suse.de
- removed libhistory.a & libreadline.a from file list.
* Wed Nov 12 1997 - ro@suse.de
- minor changes in specfile
  setting host to ARCH-suse-linux
* Mon Nov 10 1997 - ro@suse.de
- new version 2.0.9
* Tue Oct 07 1997 - ro@suse.de
- prepared spec file
- added README-GCC-2.7.? patches
