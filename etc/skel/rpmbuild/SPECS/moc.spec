Name: moc
Summary: Music on Console - Console audio player for Linux/UNIX
Version: 2.4.4 
Release: 2%{dist}
License: GPLv3+
Group: Applications/Multimedia
URL: http://moc.draper.net
Source: ftp://ftp.daper.net/pub/soft/moc/stable/moc-%{version}.tar.bz2
Patch0: moc-2.4.4-libavformat.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: ncurses alsa-lib 
BuildRequires: ncurses-devel alsa-lib-devel
# For audio codecs
BuildRequires: libsndfile-devel libmpcdec-devel libmad-devel
BuildRequires: taglib-devel libid3tag-devel ffmpeg-devel
BuildRequires: libogg-devel libvorbis-devel speex-devel flac-devel
# For network streaming support
BuildRequires: libcurl-devel
# For JACK (low-latency audio server) support
BuildRequires: jack-audio-connection-kit-devel
# For resampling of bit-rates your hw doesn't support
BuildRequires: libsamplerate-devel

%description
MOC (music on console) is a console audio player for LINUX/UNIX designed to be
powerful and easy to use. You just need to select a file from some directory
using the menu similar to Midnight Commander, and MOC will start playing all
files in this directory beginning from the chosen file.


%prep
%setup

%patch0 -p1

%build
%configure

%{__make} %{?_smp_mflags}
			
%install
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
%makeinstall
%{__rm} -rf $RPM_BUILD_ROOT/usr/share/doc/moc
mkdir -p $RPM_BUILD_ROOT%{_libdir}/moc/decoder_plugins
mv $RPM_BUILD_ROOT%{_libdir}/*.so $RPM_BUILD_ROOT%{_libdir}/moc/decoder_plugins
rm -f $RPM_BUILD_ROOT%{_libdir}/*.*a

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"

%post
/sbin/ldconfig

%postun
/sbin/lconfig

%files
%defattr(-, root, root)
%doc README COPYING config.example keymap.example
%{_bindir}/*
%{_datadir}/%{name}/*
%{_mandir}/*/*
%{_libdir}/%{name}/decoder_plugins/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/decoder_plugins

%changelog

* Mon Mar 29 2010 Will Elliott <astroidblueheaven@gmail.com> - 2.4.4-2
- patched lines 403 - 406 to fix the libav ffmpeg compile bug
- +CPPFLAGS_saved="$CPPFLAGS"
- +CPPFLAGS="$CPPFLAGS $libavformat_CFLAGS"
- -AC_CHECK_HEADERS(ffmpeg/avformat.h libavformat/avformat.h)
- +CPPFLAGS="$CPPFLAGS_saved"

* Sun Jan 31 2010 Paul Miller <paul_artichoke@yahoo.com> - 2.4.4-1
- first build for F12
