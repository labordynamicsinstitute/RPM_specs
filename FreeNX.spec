#
# spec file for package FreeNX (Version 0.4.4)
#
# Copyright (c) 2005 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://www.suse.de/feedback/
#

# norootforbuild
# neededforbuild  

BuildRequires: aaa_base acl attr bash bind-utils bison bzip2 coreutils cpio cpp cracklib cvs cyrus-sasl db devs diffutils e2fsprogs file filesystem fillup findutils flex gawk gdbm-devel glibc glibc-devel glibc-locale gpm grep groff gzip info insserv less libacl libattr libgcc  libselinux libstdc++ libxcrypt  m4 make man mktemp module-init-tools ncurses ncurses-devel net-tools netcfg openldap2-client openssl pam pam-modules patch permissions popt procinfo procps psmisc pwdutils rcs readline sed strace syslogd sysvinit tar tcpd texinfo timezone unzip util-linux vim zlib zlib-devel autoconf automake binutils gcc gdbm gettext libtool perl rpm

Name:         FreeNX
License:      GPL
URL:          http://debian.tu-bs.de/knoppix/nx/
Group:        System/X11/Servers/XF86_4
Version:      0.4.4
Release:      3.1
Requires:     NX openssh expect netcat
Summary:      FreeNX Application and Thin Client Server
Source:       freenx-%{version}.tar.gz
Source1:      README.SuSE
Source2:      ANNOUNCE-0.3.0
Source3:      ANNOUNCE-0.3.1
Source4:      ANNOUNCE-0.4.0
Source5:      ANNOUNCE-0.4.1
Source6:      ANNOUNCE-0.4.2
Source7:      NX-Firewall.txt
Patch:        freenx-enable_rootless_mode.diff
Patch1:       freenx-enable_backend.diff
Patch2:       freenx-%{version}.diff
BuildRoot:    %{_tmppath}/%{name}-%{version}-build

%description
FreeNX application and thin client server based on NX technology
NoMachine. NX is the next-generation X compression and roundtrip
suppression scheme. It can operate remote X11 sessions over 56k modem
dial-up links or anything better. This package contains a free (GPL)
implementation of the nxserver component.



Authors:
--------
    Fabian Franz <nxserver@fabian-franz.de>

%debug_package
%prep
%setup -n freenx-%{version}
%patch -p1
%patch1 -p0
%patch2 -p0

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 nx* $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/nxserver
install -m 644 node.conf.sample $RPM_BUILD_ROOT/etc/nxserver/node.conf
cp $RPM_SOURCE_DIR/{README.SuSE,ANNOUNCE-*,NX-Firewall.txt} .

%files
%defattr(-,root,root)
%doc README.SuSE AUTHORS CONTRIB COPYING ChangeLog INSTALL ANNOUNCE-* NX-Firewall.txt
%dir /etc/nxserver
%config /etc/nxserver/node.conf
/usr/bin/nxclient
/usr/bin/nxkeygen
/usr/bin/nxnode
/usr/bin/nxnode-login
/usr/bin/nxserver
/usr/bin/nxsetup
/usr/bin/nxloadconfig
/usr/bin/nxprint

%changelog -n FreeNX
* Mon Sep 05 2005 - sndirsch@suse.de
- added firewall doc (wgottwalt)
* Fri Aug 19 2005 - sndirsch@suse.de
- freenx-0.4.4.diff:
  * fixed nxsetup, when nx user does not exist yet
* Wed Aug 10 2005 - sndirsch@suse.de
- updated to FreeNX 0.4.4 "UKUUG Enterprise Edition"
  * Added ENABLE_1_5_0_BACKEND configuration directive:
  * Fixed fullscreen support in nxdesktop (still feels more
  like 'Available Area', but with Ctrl-Alt-F you can get
  "real" fullscreen)
  * Added COMMAND_MD5SUM directive
  * Security: $USER_FAKE_HOME/.nx now gets 0700
  * Fixed support for CUPS forwarding.
  * Added secure re-transmitting to client.
  * Removed grep from getent to not search through the whole
  database.
  (Suggestion by "Matthew S. Harris" <mharris@google.com>,
  "Ed Warnicke"       <eaw@cisco.com>)
  * Set sleeps to 60 instead of 10 seconds, removed one wrong trap.
  (Suggestion by "Sunil" <funtoos@yahoo.com>)
  * Made automatic timeout configurable.
  (Patch by "Ed Warnicke" <eaw@cisco.com>)
  * Made nxsetup more enterprise friendly. Added --localuser
  (RedHat only) and --gid.
  (Based on a patch by "Ed Warnicke" <eaw@cisco.com>)
  * Fixed resume of multiple sessions.
* Sat Jul 30 2005 - sndirsch@suse.de
- updated README.SuSE for FreeNX > 0.2.x
* Fri Jul 29 2005 - sndirsch@suse.de
- the option right below was commented out - fixed now
* Thu Jul 28 2005 - sndirsch@suse.de
- updated to FreeNX 0.4.3
- freenx-enable_backend.diff:
  * enables fake cookie authentication, when a 1.5.0 client connects
* Tue Jul 26 2005 - sndirsch@suse.de
- added announcement for 0.4.2 to docs
* Mon Jul 25 2005 - sndirsch@suse.de
- updated to FreeNX 0.4.2
* Sat Jul 23 2005 - sndirsch@suse.de
- freenx-enable_rootless_mode.diff:
  * enabled rootless mode by default; supported since NX 1.5.0
  Snapshot 2
* Wed Jun 29 2005 - sndirsch@suse.de
- 24.06.2005 FreeNX 0.4.1 "LinuxTag Edition"
  * Fixed a small security problem giving access to session
  database.
  * Added support for 1.5.0 OSS components. (especially rootless
  mode)
  * Fixed Filesharing over the Internet. (Thanks to
  rogierm@users.berlios.de)
  * Fixed Resume on Windows with non-fullscreen sessions.
  * Added suspend/resume support for 1.5.0 OSS components.
  * Fixed display of suspended sessions in nxserver --list.
* Thu May 12 2005 - sndirsch@suse.de
-use norootforbuild
* Wed May 11 2005 - sndirsch@suse.de
- added announcement for 0.4.0 to docs
* Thu May 05 2005 - sndirsch@suse.de
- updated to release 0.4.0:
  * obsoletes freenx-0.3.1.diff
* Thu Apr 28 2005 - sndirsch@suse.de
- freenx-0.3.1.diff:
  * nxsetup: fix permissions, fix filename of sshd init script
* Mon Mar 21 2005 - sndirsch@suse.de
- updated to release 0.3.1 ("Bugfix Edition")
  * Fixed keyboard mapping problems.
  * Fixed unix-custom mode; now allowing parameters to be passed.
  * Fixed password prompt detection support in nxnode-login.
  * Fixed locking to prevent usage of the same display.
  * Fixed resume when agent is no longer there.
  * Fixed error message shown to user, when session startup fails.
  * Fixed handling of /tmp/.X*-lock files.
  * Fixed handling of not closed sessions in "Terminating" status.
  * Fixed resume of multiple suspended sessions.
* Sun Mar 06 2005 - sndirsch@suse.de
- updated to release 0.3.0
  * Security enhancements
  * Many bugfixes
  * Single application mode works now (both, in rootless and in
  proxy mode)
  * Much improved nxsetup and nxsetup --uninstall
  * Rewrite of authentication code
  * Systemwide as well as user specific configuration files which
  are mostly compatible with NoMachine's commercial nxserver
  node.conf.
  * Changed nx home directory to /var/lib/nxserver/home and nx
  logfile to /var/lib/nxserver.log (FHS compatible)
  * Autostart and exported configuration variables for nxnode
  * Forwarding of connections to other NX servers
- obsoletes freenx-0.2.7.diff, freenx-0.2.8.diff, geom-fix.diff
- added announcement for 0.3.0 to docs
* Tue Feb 15 2005 - sndirsch@suse.de
- geom-fix.diff:
  * fix for Windows resume problems
* Mon Feb 14 2005 - sndirsch@suse.de
- README.SuSE: improved documentation once more (Bug #50714)
* Sat Feb 12 2005 - sndirsch@suse.de
- README.SuSE: improved documentation (Bug #50714)
* Sat Feb 12 2005 - sndirsch@suse.de
- fixed version number in specfile
* Fri Feb 11 2005 - sndirsch@suse.de
- freenx-0.2.8.diff:
  * Security: Fixed a security blunder. Authority file was not used
  and so basically xhost +localhost was set.
  * Security: Fixed two possible security problems (umask was not
  set correctly)
* Fri Dec 03 2004 - sndirsch@suse.de
- README.SuSE:
  * added KNOWN ISSUES section (suspend/resume problem with knx,
  Bug #48753)
* Mon Nov 29 2004 - sndirsch@suse.de
- freenx-0.2.7.diff:
  * use absolute path for nxnode-login
* Mon Nov 22 2004 - sndirsch@suse.de
- updated to release 0.2.7
  * Fix nxserver to work again with KNX-Client. ('\r' is evil)
  * Fix timeout in nxnode-login to allow proper session management
  again.
  * Fixed possible race condition for the wait-file.
- obsoletes freenx-0.2.6.diff
* Tue Nov 16 2004 - sndirsch@suse.de
- freenx-0.2.6.diff
  * workaround to fix FreeNX for use with knx; the problem is that
  expect adds Carriage Return, which knx cannot handle, but there
  is still another problem with the input buffer, which is more
  difficult to resolve ...
* Thu Nov 11 2004 - sndirsch@suse.de
- updated to release 0.2.6
  * Security: Fixed a possible exploit in ssh-usage
  thanx to Sebastian Krahmer from the SuSE security team)
  * Important: Public/Private key is no longer used for PAM auth
  mode.
  "The second change is the more interesting change. From now on
  it is possible to use FreeNX without the second login mechanism
  to ever use the public/private-key authentication.
  This efficiently removes the "Single-Point-Of-Failure" often
  criticized by different people.
  You can now remove the public keys (see
  $NX_ETC_DIR/users.id_dsa.pub) from your users
  ~/.ssh/authorized_keys2 as the system private key is no longer
  needed to login the users."
* Tue Oct 26 2004 - sndirsch@suse.de
- updated to release 0.2.5
  * Added Xdialog interface for nxclient and automatic usage
  of commercial nxclient when available. (Thx go to Rick Stout
  <zipsonic@gmail.com>)
  * Added bugfix from the 0.3.0 branch for more flexible nxdesktop in
  nxnode.
  * Added patch by Rick Stout for permission problems in nxnode.
  * Added patch by Rick Stout for a typo in nxkeygen.
  * Updated gentoo-nomachine.diff.
  * Updated CONTRIB to include a description of lazy-image encoding.
* Sun Sep 12 2004 - sndirsch@suse.de
- updated to release 0.2.4
  * Added timeout to avoid having hanging tail processes.
  * Added "locking" of the display-offset if nxagent failed to
  start.
  * Fixed ssh encryption for resume on client 1.4.0-snapshot 5.
  * Fixed mktemp, which was non-portable to FreeBSD and Red Hat 9.
* Sat Sep 11 2004 - sndirsch@suse.de
-  updated to release 0.2-3
  * Added support for autoreconnection or autoreconnection just
  for the case when an older client version is used. This makes
  it possible to use Reconnection with the stable version
  1.3.2-7 (enabled by default)
  * Added instructions how to install the NoMachine sources to
  INSTALL
  * Changed $NX_DIR/bin/ssh to ssh to fix gentoo-nomachine.diff
  * Added nxkeygen by Stuart Herbert for easier change from the
  NoMachine key to another key afterwards.
  * Security: Any user was able to change the status of other
  sessions in the session database by providing the correct
  uniqueid.
* Fri Sep 10 2004 - sndirsch@suse.de
- updated to release 0.2-2
  * Added additional support for safe session suspend,
  autosuspend when network connection times out works now!
  * AuthorizedKeysFile cannot be safely determined on Gentoo;
  changed it to config option now.
  * Added config option to completely disable passdb support.
  * Fixed bugs in nxclient dialog frontend.
  * Removed all usage of nxssh due to security concerns from SuSE.
  * Fixed session management for knx client.
  * Added detection of failed nxagent startup.
  * Updated the gentoo-nomachine.diff to be not fuzzy.
- removed freenx-0.2-1.diff (fixed upstream now)
- added netcat (replaces nxssh) as Requires
* Wed Sep 08 2004 - sndirsch@suse.de
- updated to release 0.2-1:
  * Fixed support for one windows client version.
  * Fixed setting of key with --adduser.
  (Thanks to Stuart Herbert <stuart@gentoo.org>)
  * Fixed _some_ cases for AuthorizedKeysFile in sshd_config.
  (Thanks to Peter Holik <peter@holik.at>)
  * Fixed gentoo-nomachine.diff (nxnode not in path, but nxnode-login
  would try that)
  * Fixed the bug with hanging tail processes.
- freenx-0.2-1.diff:
  * fixes typos in nxsetup
* Tue Sep 07 2004 - sndirsch@suse.de
- README.SuSE:
  * private key generated for the "nx" user by nxsetup needs to be
  distributed
* Tue Sep 07 2004 - sndirsch@suse.de
- updated to release 0.2
  * Changelog:
- Reworked the whole security model in nxsetup due to requests
  from SuSE and Gentoo.
  * nxsetup does not use the NoMachine key by default.
  * PAM authentication is enabled by default.
- Added nxclient for compatibility with nxclient -dialog mode.
- Minor changes
  * Added SSHD_AUTH_PORT to config vars in nxserver
  * Made all programs NX_ aware
  * Programs do now honor the setting of AuthorizedKeysFile in sshd_config
  * Changed nxsetup check from direct reading of passwd to getent
  (Thanks to Tom Hibbert <tom@nsp.co.nz>)
  * Changed overall messages in nxsetup
- Made a overall clean upstream package.
- Added Gentoo / NoMachine compatibility diff
  * obsoletes patches nx-0.1-2.diff, nx-0.1-4.diff,
  nxserver_0.1-2.diff.gz, nxuseradd.diff
  * adjusted README.SuSE
- added nxclient to filelist
- removed dummy manual page for nxserver
- added some docs (AUTHORS, COPYING, ChangeLog, INSTALL)
* Mon Sep 06 2004 - sndirsch@suse.de
- nxuseradd.diff:
  * fixed creating of nx user
* Mon Sep 06 2004 - sndirsch@suse.de
- nx-0.1-4.diff:
  * added pam authentication
  * added user_db switch
  * moved some su - to nxnode-login
- added nxnode-login to filelist
- added expect to Requires
- README.SuSE:
  * added documentation for PAM_AUTH
* Thu Sep 02 2004 - sndirsch@suse.de
- README.SuSE:
  * knxclient --> knx
* Thu Sep 02 2004 - sndirsch@suse.de
- nx-0.1-2.diff:
  * This package is (or at least should be) compatible with all
  nxclient Versions available since 1.3.0, but if a newer client
  version does connect (1.4.0-43 for example), it uses the new
  SSH encryption mechanism. (nxssh -B for example)
- improved README.SuSE
* Wed Sep 01 2004 - sndirsch@suse.de
- added nxserver manual page
* Wed Sep 01 2004 - sndirsch@suse.de
- created package
