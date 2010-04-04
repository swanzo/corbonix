Name:           nitrogen
Version:        1.5.1
Release:        1%{?dist}
Summary:        A background browser and setter for X windows

Group:          User Interface/Desktops
# Code is GPLv2, icons are CC-BY-SA as described in COPYING
License:        GPLv2 and CC-BY-SA
URL:            http://projects.l3ib.org/nitrogen/
Source0:        http://projects.l3ib.org/%{name}/files/%{name}-%{version}.tar.gz
Source1:        nitrogen.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  gtkmm24-devel
BuildRequires:  libpng-devel
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  desktop-file-utils
Requires:       gtkmm24

%description
A background browser and setter for X windows that can be used in two
modes: browser and recall. It features Multihead and Xinerama awareness,
a recall mode to be used in startup scripts, uses the freedesktop.org
standard for thumbnails, can set the GNOME background, command line set
modes for use in scripts, inotify monitoring of browse directory, lazy
loading of thumbnails to conserve memory and an 'automatic' set mode
which determines the best mode to set an image based on its size.


%prep
%setup -q


%build
%configure --disable-dependency-tracking
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}


%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ] ; then
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi


%files
%defattr(-,root,root,-)
%doc COPYING NEWS README AUTHORS ChangeLog
%{_bindir}/nitrogen
%{_datadir}/icons/hicolor/128x128/apps/nitrogen.png
%{_datadir}/icons/hicolor/16x16/actions/wallpaper-centered.png
%{_datadir}/icons/hicolor/16x16/actions/wallpaper-scaled.png
%{_datadir}/icons/hicolor/16x16/actions/wallpaper-tiled.png
%{_datadir}/icons/hicolor/16x16/actions/wallpaper-zoomed.png
%{_datadir}/icons/hicolor/16x16/apps/nitrogen.png
%{_datadir}/icons/hicolor/16x16/devices/video-display.png
%{_datadir}/icons/hicolor/16x16/mimetypes/image-x-generic.png
%{_datadir}/icons/hicolor/22x22/apps/nitrogen.png
%{_datadir}/icons/hicolor/32x32/apps/nitrogen.png
%{_datadir}/icons/hicolor/48x48/apps/nitrogen.png
%{_datadir}/applications/nitrogen.desktop
%{_mandir}/man1/nitrogen.1.gz


%changelog
* Fri Feb 05 2010 Sandro Mathys <red at fedoraproject.org> - 1.5.1-1
- new version with fixed licensing and some bugfixes
- added desktop file and updating of the icon caches

* Thu Oct 22 2009 Sandro Mathys <red at fedoraproject.org> - 1.4-1
- initial build

