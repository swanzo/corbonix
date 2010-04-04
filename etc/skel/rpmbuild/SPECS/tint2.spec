Name:           tint2
Version:        0.9
Release:        1%{?dist}
Summary:        A lightweight X11 desktop panel and task manager

Group:          User Interface/Desktops
License:        GPLv2
URL:            http://code.google.com/p/tint2
Source0:        http://%{name}.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:         tint2-0.9.ldlink.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  imlib2-devel pango-devel cairo-devel libXinerama-devel libXdamage-devel libXcomposite-devel libXrender-devel

%description
tint2 is a simple X11 desktop panel and taskbar intentionally made for
openbox3, but that should work with other window managers.  tint2 is intended
to be unintrusive and light in resource utilization, while following
freedesktop specifications.

%prep
%setup -q
%patch0 -p1 -b .ldlink

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_docdir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%dir %{_sysconfdir}/xdg/%{name}/
%config(noreplace) %{_sysconfdir}/xdg/%{name}/tint2rc
%{_bindir}/tint2
%{_datadir}/tint2/default_icon.png
%{_mandir}/man1/tint2.1.*

%changelog
* Sat Feb 13 2010 Chess Griffin <chess@chessgriffin.com> 0.9-1
- Update to source version 0.9.
- Add libXcomposite, libXdamage, and libXrender as build depends.
- Add patch to fix DSO linking issue.
- Remove two sed invocations.
- Add default_icon.png to files.

* Mon Aug 03 2009 Chess Griffin <chess@chessgriffin.com> 0.7.1-2
- Remove docdir from configure, and instead add rm -rf docdir after
  install.
- Add COPYING to docs.
- Remove .gz from end of man page and make it a wildcard in case
  compression format changes.

* Mon Aug 03 2009 Chess Griffin <chess@chessgriffin.com> 0.7.1-1
- Initial RPM release.
