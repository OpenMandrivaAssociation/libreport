%{!?python_site: %define python_site %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")}
# platform-dependent
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define _disable_ld_no_undefined 1
%define Werror_cflags %nil

%define _with_tests 0

Summary: Generic library for reporting various problems
Name: libreport
Version: 2.0.8
Release: 1
License: GPLv2+
Group: System/Libraries
URL: https://fedorahosted.org/abrt/
Source0: https://fedorahosted.org/released/abrt/%{name}-%{version}.tar.gz
Patch0: 0001-allow-to-specify-bodh-url-and-fix-one-NULL-dereferen.patch
Patch1: 0002-if-better-backtrace-is-avail-then-upload-one.patch
Patch2: 0003-search-only-by-duphash-for-selinux.patch
Patch3: 0004-reorganize-comments-for-bugzilla-message-body-comes-.patch
Patch4: 0005-do-not-insert-duplicate-comment-to-bugzilla.patch
Patch5: 0006-if-OSRelease-environ-is-empty-load-OSRelease-from-pr.patch
Patch6: 0009-bodhi-sync-enum-with-parse_opt.patch
Patch7: 0010-inicializing-rpm-more-then-once-leads-to-sigsegv-in-.patch
Patch8: 0011-url-takes-escaped-string.patch
Patch9: 0001-rhbz-add-the-architecture-to-the-comment-only-if-it-.patch
Patch10: 0001-rhbz-768647-python-doen-t-have-a-backtrace_rating-fi.patch

Patch100:      libreport-2.0.8-add-mandriva-support.patch
Patch101:	libreport-2.0.8-link.patch
Patch102:	libreport-2.0.8-rpm5.patch
BuildRequires: dbus-devel
BuildRequires: gtk2-devel
BuildRequires: curl-devel
BuildRequires: desktop-file-utils
BuildRequires: xmlrpc-c-devel
BuildRequires: python-devel
BuildRequires: gettext
BuildRequires: libxml2-devel
BuildRequires: libtar-devel
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: nss-devel
BuildRequires: texinfo
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: newt-devel
BuildRequires: libproxy-devel
BuildRequires: libgnome-keyring-devel
BuildRequires: docbook-style-xsl
Requires: libreport-filesystem
Requires: libreport-python = %{version}-%{release}

%description
Libraries providing API for reporting different problems in applications
to different bug targets like Bugzilla, ftp, trac, etc...

%files -f %{name}.lang
%doc README COPYING
%config(noreplace) %{_sysconfdir}/%{name}/report_event.conf
%exclude %_libdir/libabrt_web.so
%exclude %{_mandir}/man1/reporter-rhtsupport.1.*
%{_mandir}/man5/report_event.conf.5*

#--------------------------------------------------------------------

%define lib_major_dbus 0
%define libname_dbus %mklibname report-abrt_dbus %{lib_major_dbus}

%package -n %libname_dbus
Summary: GTK front-end for libreport
Group:   System/Libraries

%description -n %libname_dbus
Applications for reporting bugs using libreport backend

%files -n %libname_dbus
%{_libdir}/libabrt_dbus.so.%{lib_major_dbus}*

#--------------------------------------------------------------------

%define lib_major_web 0
%define libname_web %mklibname report-abrt_web %{lib_major_web}

%package -n %libname_web
Summary: GTK front-end for libreport
Group:   System/Libraries

%description -n %libname_web
Applications for reporting bugs using libreport backend

%files -n %libname_web
%{_libdir}/libabrt_web.so.%{lib_major_web}*

#--------------------------------------------------------------------

%define lib_major 0
%define libname %mklibname report %{lib_major}

%package -n %libname
Summary: GTK front-end for libreport
Group:   System/Libraries

%description -n %libname
Applications for reporting bugs using libreport backend

%files -n %libname
%{_libdir}/libreport.so.%{lib_major}*

#--------------------------------------------------------------------

%package filesystem
Summary: Filesystem layout for libreport
Group:   File tools

%description filesystem
Filesystem layout for libreport

%files filesystem
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/events.d/
%dir %{_sysconfdir}/%{name}/events/
%dir %{_sysconfdir}/%{name}/plugins/

#--------------------------------------------------------------------

%define lib_name_devel %mklibname report -d

%package -n %lib_name_devel
Summary:  Development libraries and headers for libreport
Group:    Development/C
Requires: libreport = %{version}-%{release}
Requires: %libname_dbus = %{version}-%{release}
Requires: %libname_web = %{version}-%{release}
Requires: %libname = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %lib_name_devel
Development libraries and headers for libreport

%files -n %lib_name_devel
# Public api headers: 
%{_includedir}/libreport/client.h
%{_includedir}/libreport/dump_dir.h
%{_includedir}/libreport/event_config.h
%{_includedir}/libreport/problem_data.h
%{_includedir}/libreport/report.h
%{_includedir}/libreport/run_event.h
# Private api headers:
%{_includedir}/libreport/internal_abrt_dbus.h
%{_includedir}/libreport/internal_libreport.h
%{_libdir}/libreport.so
%{_libdir}/libabrt_web.so
%{_libdir}/libabrt_dbus.so
%{_libdir}/pkgconfig/libreport.pc
%dir %{_includedir}/libreport

#--------------------------------------------------------------------

%package python
Summary: Python bindings for report-libs
# Is group correct here? -
Group: System/Libraries
Requires: libreport = %{version}-%{release}
Provides: report = 0.23-1
Obsoletes: report < 0.23-1

%description python
Python bindings for report-libs.

%files python
%{python_sitearch}/report/*
%{python_sitearch}/reportclient/*

#--------------------------------------------------------------------

%package cli
Summary: %{name}'s command line interface
Group:   Graphical desktop/Other 
Requires: %{name} = %{version}-%{release}

%description cli
This package contains simple command line tool for working
with problem dump reports

%files cli
%{_bindir}/report-cli
%{_mandir}/man1/report-cli.1.*
%{_mandir}/man1/reporter-rhtsupport.1.*

#--------------------------------------------------------------------

%package newt
Summary: %{name}'s newt interface
Group:   Graphical desktop/Other 
Requires: %{name} = %{version}-%{release}
Provides: report-newt = 0.23-1
Obsoletes: report-newt < 0.23-1

%description newt
This package contains a simple newt application for reporting
bugs

%files newt
%{_bindir}/report-newt

#--------------------------------------------------------------------

%package gtk
Summary: GTK front-end for libreport
Group:   Graphical desktop/GNOME
Requires: libreport = %{version}-%{release}
Provides: report-gtk = 0.23-1
Obsoletes: report-gtk < 0.23-1

%description gtk
Applications for reporting bugs using libreport backend

%files gtk
%{_bindir}/report-gtk


#--------------------------------------------------------------------

%define lib_major_gtk 0
%define libname_gtk %mklibname report-gtk %{lib_major_gtk}

%package -n %libname_gtk
Summary: GTK front-end for libreport
Group:   System/Libraries

%description -n %libname_gtk
Applications for reporting bugs using libreport backend

%files -n %libname_gtk
%{_libdir}/libreport-gtk.so.%{lib_major_gtk}*

#--------------------------------------------------------------------

%define lib_namegtk_devel %mklibname report-gtk -d

%package -n %lib_namegtk_devel
Summary: Development libraries and headers for libreport
Group:   Development/GNOME and GTK+ 
Requires: libreport-gtk = %{version}-%{release}
Requires: %libname_gtk = %{version}-%{release}
Provides: %name-gtk-devel = %{version}-%{release}

%description -n %lib_namegtk_devel
Development libraries and headers for libreport-gtk

%files -n %lib_namegtk_devel
%{_libdir}/libreport-gtk.so
%{_includedir}/libreport/internal_libreport_gtk.h
%{_libdir}/pkgconfig/libreport-gtk.pc

#--------------------------------------------------------------------

%package plugin-kerneloops
Summary: %{name}'s kerneloops reporter plugin
Group: System/Libraries
Requires: curl
Requires: %{name} = %{version}-%{release}

%description plugin-kerneloops
This package contains plugin which sends kernel crash information to specified
server, usually to kerneloops.org.

%files plugin-kerneloops
%{_sysconfdir}/libreport/events/report_Kerneloops.xml
%{_mandir}/man*/reporter-kerneloops.*
%{_bindir}/reporter-kerneloops

#--------------------------------------------------------------------

%package plugin-logger
Summary: %{name}'s logger reporter plugin
Group: System/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-logger < 2.0.4
Provides: report-plugin-localsave = 0.23-1
Obsoletes: report-plugin-localsave < 0.23-1
Provides: report-config-localsave = 0.23-1
Obsoletes: report-config-localsave < 0.23-1

%description plugin-logger
The simple reporter plugin which writes a report to a specified file.

%files plugin-logger
%{_sysconfdir}/libreport/events/report_Logger.conf
%{_sysconfdir}/libreport/events/report_Logger.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/print_event.conf
%{_bindir}/reporter-print
%{_mandir}/man*/reporter-print.*

#--------------------------------------------------------------------

%package plugin-mailx
Summary: %{name}'s mailx reporter plugin
Group: System/Libraries
Requires: %{name} = %{version}-%{release}
Requires: mailx
Obsoletes: abrt-plugin-mailx < 2.0.4

%description plugin-mailx
The simple reporter plugin which sends a report via mailx to a specified
email address.

%files plugin-mailx
%{_sysconfdir}/libreport/events/report_Mailx.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/mailx_event.conf
%{_mandir}/man*/reporter-mailx.*
%{_bindir}/reporter-mailx

#--------------------------------------------------------------------

%package plugin-bugzilla
Summary: %{name}'s bugzilla plugin
Group: System/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-bugzilla < 2.0.4
Provides: report-plugin-bugzilla = 0.23-1
Obsoletes: report-plugin-bugzilla < 0.23-1
Provides: report-config-bugzilla-redhat-com = 0.23-1
Obsoletes: report-config-bugzilla-redhat-com < 0.23-1

%description plugin-bugzilla
Plugin to report bugs into the bugzilla.

%files plugin-bugzilla
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla.conf
%{_sysconfdir}/libreport/events/report_Bugzilla.xml
%config(noreplace) %{_sysconfdir}/libreport/events/report_Bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/bugzilla_event.conf
# FIXME: remove with the old gui
%{_mandir}/man1/reporter-bugzilla.1.*
%{_bindir}/reporter-bugzilla

#--------------------------------------------------------------------

%package plugin-bodhi
Summary: %{name}'s bodhi plugin
BuildRequires: json-c-devel
Group: System/Libraries
Requires: %{name} = %{version}-%{release}
Requires: packagekit
BuildRequires: rpm-devel

%description plugin-bodhi
Search for a new updates in bodhi server

%files plugin-bodhi
%{_bindir}/abrt-bodhi
%{_mandir}/man1/abrt-bodhi.1.*

#--------------------------------------------------------------------

%package compat
Summary: %{name}'s compat layer for obsoleted 'report' package
Group: System/Libraries
Requires: %{name}-plugin-bugzilla

%description compat
Provides 'report' command-line tool.

%files compat
%{_bindir}/report
%{_mandir}/man1/report.1.*

#--------------------------------------------------------------------

%package plugin-reportuploader
Summary: %{name}'s reportuploader plugin
Group: System/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-reportuploader < 2.0.4
Provides: report-plugin-ftp = 0.23-1
Obsoletes: report-plugin-ftp < 0.23-1
Provides: report-config-ftp = 0.23-1
Obsoletes: report-config-ftp < 0.23-1
Provides: report-plugin-scp = 0.23-1
Obsoletes: report-plugin-scp < 0.23-1
Provides: report-config-scp = 0.23-1
Obsoletes: report-config-scp < 0.23-1

%description plugin-reportuploader
Plugin to report bugs into anonymous FTP site associated with ticketing system.

%files plugin-reportuploader
%{_mandir}/man*/reporter-upload.*
%{_bindir}/reporter-upload
%{_sysconfdir}/libreport/events/report_Uploader.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/uploader_event.conf
#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
autoconf
%configure
CFLAGS="-fno-strict-aliasing"
%make

%install
make install DESTDIR=%buildroot mandir=%{_mandir}
%find_lang %{name}

# remove all .la and .a files
find %buildroot -name '*.la' -or -name '*.a' | xargs rm -f
mkdir -p %buildroot/%{_initrddir}
mkdir -p %buildroot/%{_sysconfdir}/%{name}/events.d/
mkdir -p %buildroot/%{_sysconfdir}/%{name}/events/

# After everything is installed, remove info dir
rm -f %buildroot/%{_infodir}/dir

rm -f %buildroot/%{_sysconfdir}/libreport/plugins/rhtsupport.conf
rm -f %buildroot/%{_sysconfdir}/libreport/events/report_RHTSupport.xml
rm -f %buildroot/%{_sysconfdir}/libreport/events.d/rhtsupport_event.conf
rm -f %buildroot/%{_mandir}/man1/reporter-rhtsupport.1.*
rm -f %buildroot/%{_mandir}/man1/reporter-rhtsupport.1.xz
rm -f %buildroot/%{_bindir}/reporter-rhtsupport

%if %_with_tests
%check
make check
%endif
