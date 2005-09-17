Name: yarrs
License: GPL
Group: System Environment/Daemons;Multimedia
Summary: Provides the Rio server software
Packager: Lars Vilhuber <lars.vilhuber@cloutier-vilhuber.net>
Version: 1.1
Release: jan
Source0: yarrs-1.1-jan.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-build 
BuildArch: i586

%description
This is the Yarrs server (source lost), modified by Jan Vilhuber.
It contains the full Rio player nfs mount.

%prep
%setup 

%build

%install
cp -a * %buildroot

%clean
rm -rf %buildroot

%files
%config
/etc/sysconfig/rio-yarrs.conf
/etc/exports.rio-yarrs
/etc/apache2/conf.d/rio-httpd.conf


/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/_build/build_params
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/_build/cleanup
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/_build/notes
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/_build/prereqs
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/blib/lib/AudioFile/Info.pm
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/blib/libdoc/AudioFile::Info.3pm
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/lib/AudioFile/Info.pm
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/t/1.t
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/Build
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/Build.PL
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/Changes
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/MANIFEST
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/META.yml
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/Makefile
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/Makefile.PL
/usr/local/yarrs-1.1-jan/AudioFile-Info-1.05/README
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/blib/arch/auto/MP3/Info/.exists
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/blib/lib/MP3/.exists
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/blib/lib/MP3/Info.pm
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/blib/lib/MPEG/MP3Info.pm
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/blib/lib/auto/MP3/Info/.exists
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/blib/man3/.exists
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/blib/man3/MP3::Info.3pm
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/blib/man3/MPEG::MP3Info.3pm
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/eg/mp3tag.PL
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/eg/mp3tocddb.PL
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/lib/MPEG/MP3Info.pm
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/getset.t
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/id3.t
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/lame-info.t
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/remove.t
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/test1.mp3
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/test2.mp3
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/testv1.1.mp3
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/testv1.mp3
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/testv2.2.0.mp3
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/testv2.3.0.mp3
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/t/testv2.4.0.mp3
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/Changes
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/Info.pm
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/MANIFEST
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/Makefile
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/Makefile.PL
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/README
/usr/local/yarrs-1.1-jan/MP3-Info-1.02/pm_to_blib
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/_Inline/config
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/blib/arch/auto/Ogg/Vorbis/Header/.exists
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/blib/arch/auto/Ogg/Vorbis/Header/Header.bs
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/blib/arch/auto/Ogg/Vorbis/Header/Header.so
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/blib/lib/Ogg/Vorbis/.exists
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/blib/lib/Ogg/Vorbis/Header.pm
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/blib/lib/auto/Ogg/Vorbis/Header/.exists
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/blib/man3/.exists
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/blib/man3/Ogg::Vorbis::Header.3pm
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/inc/LICENSE.LGPL
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/inc/i18n.h
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/inc/vcedit.c
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/inc/vcedit.h
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/Changes
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/Header.inl
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/Header.pm
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/LICENSE.GPL
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/MANIFEST
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/Makefile
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/Makefile.PL
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/README
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/pm_to_blib
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/test.ogg
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/test.ogg.bak
/usr/local/yarrs-1.1-jan/Ogg-Vorbis-Header-0.03/test.pl
/usr/local/yarrs-1.1-jan/YAML-0.35/bin/phone2yaml
/usr/local/yarrs-1.1-jan/YAML-0.35/bin/phone2yaml.PL
/usr/local/yarrs-1.1-jan/YAML-0.35/bin/xyx
/usr/local/yarrs-1.1-jan/YAML-0.35/bin/xyx.PL
/usr/local/yarrs-1.1-jan/YAML-0.35/bin/yaml2outline
/usr/local/yarrs-1.1-jan/YAML-0.35/bin/yaml2outline.PL
/usr/local/yarrs-1.1-jan/YAML-0.35/bin/ysh
/usr/local/yarrs-1.1-jan/YAML-0.35/bin/ysh.PL
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/arch/auto/YAML/.exists
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/lib/YAML/Error.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/lib/YAML/Family.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/lib/YAML/Node.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/lib/YAML/Transfer.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/lib/auto/YAML/.exists
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/lib/.exists
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/lib/YAML.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/lib/YAML.pod
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/man1/.exists
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/man1/phone2yaml.1
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/man1/xyx.1
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/man1/yaml2outline.1
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/man1/ysh.1
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/man3/.exists
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/man3/YAML.3pm
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/man3/YAML::Node.3pm
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/script/.exists
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/script/phone2yaml
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/script/xyx
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/script/yaml2outline
/usr/local/yarrs-1.1-jan/YAML-0.35/blib/script/ysh
/usr/local/yarrs-1.1-jan/YAML-0.35/lib/YAML/Error.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/lib/YAML/Family.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/lib/YAML/Node.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/lib/YAML/Transfer.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/t/00basic.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/01pass.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/02fail.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/10dump.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/11code.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/12nest.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/13opts.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/20load.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/21spec.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/22slides.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/30errors.t
/usr/local/yarrs-1.1-jan/YAML-0.35/t/TestDumper.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/t/TestYAML.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/Changes
/usr/local/yarrs-1.1-jan/YAML-0.35/MANIFEST
/usr/local/yarrs-1.1-jan/YAML-0.35/Makefile
/usr/local/yarrs-1.1-jan/YAML-0.35/Makefile.PL
/usr/local/yarrs-1.1-jan/YAML-0.35/README
/usr/local/yarrs-1.1-jan/YAML-0.35/YAML.pm
/usr/local/yarrs-1.1-jan/YAML-0.35/YAML.pod
/usr/local/yarrs-1.1-jan/YAML-0.35/pm_to_blib
/usr/local/yarrs-1.1-jan/bin/rio-builddb
/usr/local/yarrs-1.1-jan/cgi-bin/Rio/Config.pm
/usr/local/yarrs-1.1-jan/cgi-bin/.dir
/usr/local/yarrs-1.1-jan/cgi-bin/.pag
/usr/local/yarrs-1.1-jan/cgi-bin/content.cgi
/usr/local/yarrs-1.1-jan/cgi-bin/favourites.cgi
/usr/local/yarrs-1.1-jan/cgi-bin/list.cgi
/usr/local/yarrs-1.1-jan/cgi-bin/query.cgi
/usr/local/yarrs-1.1-jan/cgi-bin/results.cgi
/usr/local/yarrs-1.1-jan/cgi-bin/tags.cgi
/usr/local/yarrs-1.1-jan/cron/rio-build-fix
/usr/local/yarrs-1.1-jan/etc/init.d/ssdpd
/usr/local/yarrs-1.1-jan/etc/xinetd.d/ssdp
/usr/local/yarrs-1.1-jan/etc/dhcpd.conf
/usr/local/yarrs-1.1-jan/etc/exports
/usr/local/yarrs-1.1-jan/etc/inetd.conf
/usr/local/yarrs-1.1-jan/etc/rio-httpd.conf
/usr/local/yarrs-1.1-jan/etc/services
/usr/local/yarrs-1.1-jan/etc/crontab.yarrs
/usr/local/yarrs-1.1-jan/htdocs/layout/en_UK/all_info
/usr/local/yarrs-1.1-jan/htdocs/layout/en_UK/big_title
/usr/local/yarrs-1.1-jan/htdocs/layout/en_UK/index
/usr/local/yarrs-1.1-jan/htdocs/layout/en_UK/inverse_scope
/usr/local/yarrs-1.1-jan/htdocs/layout/en_UK/remaining
/usr/local/yarrs-1.1-jan/htdocs/layout/en_UK/scope
/usr/local/yarrs-1.1-jan/htdocs/favourites.txt
/usr/local/yarrs-1.1-jan/man/man1/GNUmakefile
/usr/local/yarrs-1.1-jan/man/man8/GNUmakefile
/usr/local/yarrs-1.1-jan/man/GNUmakefile
/usr/local/yarrs-1.1-jan/man/man.mk
/usr/local/yarrs-1.1-jan/mod-jan/cgi-bin/Rio/Config.pm
/usr/local/yarrs-1.1-jan/mod-jan/cgi-bin/.dir
/usr/local/yarrs-1.1-jan/mod-jan/cgi-bin/.pag
/usr/local/yarrs-1.1-jan/mod-jan/cgi-bin/content.cgi
/usr/local/yarrs-1.1-jan/mod-jan/cgi-bin/favourites.cgi
/usr/local/yarrs-1.1-jan/mod-jan/cgi-bin/list.cgi
/usr/local/yarrs-1.1-jan/mod-jan/cgi-bin/query.cgi
/usr/local/yarrs-1.1-jan/mod-jan/cgi-bin/results.cgi
/usr/local/yarrs-1.1-jan/mod-jan/cgi-bin/tags.cgi
/usr/local/yarrs-1.1-jan/sbin/rio-ssdp
/usr/local/yarrs-1.1-jan/sbin/test-ssdp
/usr/local/yarrs-1.1-jan/sbin/rio-build-database
/usr/local/yarrs-1.1-jan/Changes
/usr/local/yarrs-1.1-jan/Copying
/usr/local/yarrs-1.1-jan/INSTALL
/usr/local/yarrs-1.1-jan/build.sh
/usr/local/yarrs-1.1-jan/log
/usr/local/yarrs-1.1-jan/rio-http.tar.gz
/usr/local/yarrs
/usr/local/sbin/rio-ssdp
/usr/local/sbin/test-ssdp
/usr/local/sbin/rio-build-database
/etc/cron.daily/rio-rebuild-cron
/etc/init.d/rc3.d/K03rio-ssdp
/etc/init.d/rc3.d/S20rio-ssdp
/etc/init.d/rc5.d/K03rio-ssdp
/etc/init.d/rc5.d/S20rio-ssdp
/etc/init.d/rio-ssdp.local
/tftpboot/default/dev/console
/tftpboot/default/dev/core
/tftpboot/default/etc/nsswitch.conf
/tftpboot/default/etc/ld.so.conf
/tftpboot/default/etc/ld.so.cache
/tftpboot/default/etc/protocols
/tftpboot/default/etc/profile
/tftpboot/default/sbin/init
/tftpboot/default/empeg/bin/player
/tftpboot/default/empeg/lib/lang/en_UK.msgso
/tftpboot/default/empeg/lib/fonts/medium.bf
/tftpboot/default/empeg/lib/fonts/timecode.bf
/tftpboot/default/empeg/lib/fonts/small.bf
/tftpboot/default/empeg/lib/fonts/wait.bf
/tftpboot/default/empeg/lib/fonts/large.bf
/tftpboot/default/empeg/lib/fonts/graphics.bf
/tftpboot/default/il-binary.o
/tftpboot/default/zImage
/tftpboot/default/zImage.orig
/tftpboot/192.168.1.151
/tftpboot/192.168.1.152
/tftpboot/192.168.1.153
/tftpboot/192.168.1.154
/tftpboot/rio

%changelog -n update_modules_dep 
* Tue Jan 25  2005 root <root@belanger> - 
- Initial build.


