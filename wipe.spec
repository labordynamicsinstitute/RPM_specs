#
# spec file for package wipe (Version 2.2.0)
#
# Copyright (c) 2007 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
# usedforbuild    aaa_base acl attr audit-libs autoconf automake bash binutils bzip2 coreutils cpio cpp cpp42 cracklib cvs diffutils file filesystem fillup findutils gawk gcc gcc42 gdbm gettext gettext-devel glibc glibc-devel glibc-locale grep groff gzip info insserv less libacl libattr libbz2-1 libbz2-devel libdb-4_5 libgcc42 libgomp42 libltdl-3 libmudflap42 libreadline5 libstdc++42 libtool libuuid1 libvolume_id libxcrypt libzio linux-kernel-headers m4 make man mktemp ncurses net-tools netcfg pam pam-modules patch perl perl-base permissions popt rpm sed sysvinit tar texinfo timezone util-linux zlib

Name:           wipe
Url:            http://wipe.sourceforge.net
License:        GPL v2 or later
Group:          Productivity/File utilities
AutoReqProv:    on
Version:        2.2.0
Release:        96
Summary:        Secure erasure of data
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-%{version}.tar.bz2.sig
Patch:          %{name}-%{version}-makefile.diff
Patch1:         %{name}-%{version}-errno.diff
Patch2:         %{name}-%{version}-include.diff
Patch3:         %{name}-%{version}-string.diff
Patch4:         %{name}-%{version}-autoconf.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
securely erase files from magnetic media



Authors:
--------
    Berke Durak <bedrettin@chez.com>

%debug_package
%prep
%setup -q
%patch
%patch1
%patch2
%patch3
%patch4

%build
%{suse_update_config -f}
autoconf
CFLAGS="$RPM_OPT_FLAGS -Wall" \
	./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--mandir=%{_mandir} \
	--datadir=%{_datadir}
make CFLAGS="$RPM_OPT_FLAGS -Wall -I. -DLINUX $(DEFINES) -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64"

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README TESTING TODO copyright
%doc %{_mandir}/man?/*
%{_bindir}/*
%changelog
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Jan 16 2006 - schwab@suse.de
- Don't strip binaries.
* Thu Jul 21 2005 - anicka@suse.cz
- fix broken path handling (#70841)
* Mon Apr 18 2005 - mjancar@suse.cz
- fix for new kernel headers
* Fri May 28 2004 - mjancar@suse.cz
- fix broken kernel includes
* Mon Mar 01 2004 - hmacht@suse.de
- building as nonroot-user
- added patch for correcting the install permissions
* Fri Feb 27 2004 - mjancar@suse.cz
- update to 2.2.0
* Wed Jun 04 2003 - mjancar@suse.cz
- update to 2.1.0
- use $RPM_OPT_FLAGS
- correct author
* Mon Dec 02 2002 - ro@suse.de
- include errno.h where needed
* Tue Sep 17 2002 - ro@suse.de
- removed bogus self-provides
* Tue Feb 12 2002 - ro@suse.de
- fixed makefile patch (wrong install options for man-page)
* Wed Aug 08 2001 - adostal@suse.cz
- update to version 2.0.0
- fixed spec file and makefile
- add .sig file to sources
* Tue Dec 05 2000 - schwab@suse.de
- Add %%suse_update_config.
* Mon Oct 23 2000 - kukuk@suse.de
- Update to wipe 1.2.2
- Don't use kernel header files
* Tue Apr 04 2000 - ro@suse.de
- added patch from homepage to avoid mmap-errors
- cleaned patch a bit
* Thu Feb 24 2000 - freitag@suse.de
- moved manpage to /usr/share
* Sat Oct 23 1999 - freitag@suse.de
- update to version 1.0.0
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Wed Aug 04 1999 - kukuk@suse.de
- Remove old binary before we call make
* Fri Nov 27 1998 - bs@suse.de
- install man page in section 8.
* Thu Nov 19 1998 - @suse.de
- new packages version 0.02
