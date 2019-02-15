%define _disable_ld_no_undefined 1
%define Werror_cflags %nil

%define _with_tests 0
%define __noautoreq 'devel\\(libxmlrpc(.*)'

%bcond_with python2

Summary:	Generic library for reporting various problems
Name:		libreport
Version:	2.10.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://github.com/abrt/libreport
Source0:	https://github.com/abrt/libreport/archive/%{version}.tar.gz

BuildRequires:	asciidoc
BuildRequires:	augeas
BuildRequires:	augeas-devel
BuildRequires:	desktop-file-utils
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRequires:	xmlto
BuildRequires:	libtar-devel
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gnome-keyring-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libnewt)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(nss)
BuildRequires:	pkgconfig(python)
BuildRequires:  pkgconfig(python3)
BuildRequires:	pkgconfig(satyr)
BuildRequires:	pkgconfig(xmlrpc)
BuildRequires:	pkgconfig(json-c)
Requires:	libreport-filesystem
Requires:	libreport-python = %{version}-%{release}

%description
Libraries providing API for reporting different problems in applications
to different bug targets like Bugzilla, ftp, trac, etc...

%files -f %{name}.lang
%license COPYING
%doc %{_docdir}/%{name}/README.md
%config(noreplace) %{_sysconfdir}/%{name}/report_event.conf
%config(noreplace) %{_sysconfdir}/%{name}/forbidden_words.conf
%config(noreplace) %{_sysconfdir}/%{name}/ignored_words.conf
%config(noreplace) %{_sysconfdir}/%{name}/events.d/centos_report_event.conf
%config(noreplace) %{_sysconfdir}/%{name}/events/report_CentOSBugTracker.conf
%config(noreplace) %{_sysconfdir}/%{name}/events/report_Uploader.conf
%config(noreplace) %{_sysconfdir}/%{name}/libreport.conf
%config(noreplace) %{_sysconfdir}/%{name}/plugins/mantisbt.conf
%config(noreplace) %{_sysconfdir}/%{name}/plugins/mantisbt_format.conf
%config(noreplace) %{_sysconfdir}/%{name}/plugins/mantisbt_format_analyzer_libreport.conf
%config(noreplace) %{_sysconfdir}/%{name}/plugins/mantisbt_formatdup.conf
%config(noreplace) %{_sysconfdir}/%{name}/plugins/mantisbt_formatdup_analyzer_libreport.conf
%config(noreplace) %{_sysconfdir}/%{name}/workflows.d/report_centos.conf
%config(noreplace) %{_sysconfdir}/%{name}/workflows.d/report_rhel_add_data.conf
%config(noreplace) %{_sysconfdir}/%{name}/workflows.d/report_uReport.conf
%{_datadir}/augeas/lenses/libreport.aug
%{_bindir}/reporter-mantisbt
%{_bindir}/reporter-systemd-journal
%dir %{_datadir}/libreport
%dir %{_datadir}/libreport/conf.d
%dir %{_datadir}/libreport/conf.d/plugins
%dir %{_datadir}/libreport/events
%dir %{_datadir}/libreport/workflows
%{_datadir}/libreport/conf.d/libreport.conf
%{_datadir}/libreport/conf.d/plugins/mantisbt.conf
%{_datadir}/libreport/events/report_CentOSBugTracker.xml
%{_datadir}/libreport/events/report_RHTSupport_AddData.xml
%{_datadir}/libreport/workflows/workflow_CentOSCCpp.xml
%{_datadir}/libreport/workflows/workflow_CentOSJava.xml
%{_datadir}/libreport/workflows/workflow_CentOSJavaScript.xml
%{_datadir}/libreport/workflows/workflow_CentOSKerneloops.xml
%{_datadir}/libreport/workflows/workflow_CentOSLibreport.xml
%{_datadir}/libreport/workflows/workflow_CentOSPython.xml
%{_datadir}/libreport/workflows/workflow_CentOSPython3.xml
%{_datadir}/libreport/workflows/workflow_CentOSVmcore.xml
%{_datadir}/libreport/workflows/workflow_CentOSXorg.xml
%{_datadir}/libreport/workflows/workflow_uReport.xml
%{_mandir}/man1/reporter-mantisbt.1.xz
%{_mandir}/man1/reporter-systemd-journal.1.xz
%{_mandir}/man5/centos_report_event.conf.5.xz
%{_mandir}/man5/libreport.conf.5.xz
%{_mandir}/man5/forbidden_words.conf.5*
%{_mandir}/man5/report_event.conf.5*
%{_mandir}/man5/ignored_words.conf.5*
%{_mandir}/man5/mantisbt.conf.5.xz
%{_mandir}/man5/mantisbt_format.conf.5.xz
%{_mandir}/man5/mantisbt_format_analyzer_libreport.conf.5.xz
%{_mandir}/man5/mantisbt_formatdup.conf.5.xz
%{_mandir}/man5/mantisbt_formatdup_analyzer_libreport.conf.5.xz
%{_mandir}/man5/report_CentOSBugTracker.conf.5.xz
%{_mandir}/man5/report_Uploader.conf.5.xz
%{_mandir}/man5/report_centos.conf.5.xz
%{_mandir}/man5/report_uReport.conf.5.xz
%{_mandir}/man5/upload.conf.5.xz

#--------------------------------------------------------------------

%define lib_major_dbus 0
%define libname_dbus %mklibname report-abrt_dbus %{lib_major_dbus}

%package -n %{libname_dbus}
Summary:	GTK front-end for libreport
Group:		System/Libraries

%description -n %{libname_dbus}
Applications for reporting bugs using libreport backend

%files -n %{libname_dbus}
%{_libdir}/libabrt_dbus.so.%{lib_major_dbus}*
%{_datadir}/dbus-1/interfaces/*.xml

#--------------------------------------------------------------------

%define lib_major_web 0
%define libname_web %mklibname report-web %{lib_major_web}

%package -n %{libname_web}
Summary:	GTK front-end for libreport
Group:		System/Libraries

%description -n %{libname_web}
Applications for reporting bugs using libreport backend

%files -n %{libname_web}
%{_libdir}/libreport-web.so.%{lib_major_web}*


#--------------------------------------------------------------------

%define libname_web_devel %mklibname report-web -d

%package -n %libname_web_devel
Summary: Development libraries and headers for libreport
Group:   Development/C
Requires: %libname_web = %{version}-%{release}
Provides: %name-web-devel = %{version}-%{release}
# (cg) The below require should be automatic, but due to the text .so files, it's not
Requires: libxmlrpc-c-devel

%description -n %libname_web_devel
Development libraries and headers for libreport-gtk

%files -n %libname_web_devel
%{_libdir}/libreport-web.so
%{_libdir}/pkgconfig/libreport-web.pc

#--------------------------------------------------------------------

%define lib_major 0
%define libname %mklibname report %{lib_major}

%package -n %{libname}
Summary:	GTK front-end for libreport
Group:		System/Libraries

%description -n %{libname}
Applications for reporting bugs using libreport backend

%files -n %{libname}
%{_libdir}/libreport.so.%{lib_major}*

#--------------------------------------------------------------------

%package filesystem
Summary:	Filesystem layout for libreport
Group:		File tools

%description filesystem
Filesystem layout for libreport

%files filesystem
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/events.d/
%dir %{_sysconfdir}/%{name}/events/
%dir %{_sysconfdir}/%{name}/plugins/

#--------------------------------------------------------------------

%define lib_name_devel %mklibname report -d

%package -n %{lib_name_devel}
Summary:	Development libraries and headers for libreport
Group:		Development/C
Requires:	libreport = %{version}-%{release}
Requires:	%{libname_dbus} = %{version}-%{release}
Requires:	%{libname_web} = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{lib_name_devel}
Development libraries and headers for libreport

%files -n %{lib_name_devel}
# Public api headers:
%{_includedir}/libreport/config_item_info.h
%{_includedir}/libreport/client.h
%{_includedir}/libreport/dump_dir.h
%{_includedir}/libreport/event_config.h
%{_includedir}/libreport/file_obj.h
%{_includedir}/libreport/problem_data.h
%{_includedir}/libreport/report.h
%{_includedir}/libreport/run_event.h
%{_includedir}/libreport/libreport_curl.h
%{_includedir}/libreport/libreport_types.h
%{_includedir}/libreport/workflow.h
%{_includedir}/libreport/xml_parser.h
%{_includedir}/libreport/problem_details_dialog.h
%{_includedir}/libreport/problem_details_widget.h
%{_includedir}/libreport/ureport.h
%{_includedir}/libreport/global_configuration.h
%{_includedir}/libreport/helpers/testsuite.h
%{_includedir}/libreport/helpers/testsuite_tools.h
%{_includedir}/libreport/problem_report.h
%{_includedir}/libreport/problem_utils.h
%{_includedir}/libreport/reporters.h
%{_includedir}/libreport/report_result.h

# Private api headers:
%{_includedir}/libreport/internal_abrt_dbus.h
%{_includedir}/libreport/internal_libreport.h
%{_libdir}/libreport.so
%{_libdir}/libabrt_dbus.so
%{_libdir}/pkgconfig/libreport.pc
%dir %{_includedir}/libreport
%dir %{_includedir}/libreport/helpers

#--------------------------------------------------------------------

%if %{with python2}
%package python2
Summary:	Python2 bindings for report-libs
# Is group correct here? -
Group:		System/Libraries
Requires:	libreport = %{version}-%{release}
Provides:	report = 0.23-1
Obsoletes:	report < 0.23-1

%description python2
Python bindings for report-libs.

%files python2
%{py2_platsitedir}/report/*
%{py2_platsitedir}/reportclient/*
%endif

#--------------------------------------------------------------------

%package python
Summary:        Python3 bindings for report-libs
# Is group correct here? -
Group:          System/Libraries
Requires:       libreport = %{version}-%{release}
Provides:       report = 0.23-1
Obsoletes:      report < 0.23-1

%description python
Python bindings for report-libs.

%files python
%{py_platsitedir}/report
%{py_platsitedir}/reportclient

#--------------------------------------------------------------------

%package cli
Summary:	%{name}'s command line interface
Group:		Graphical desktop/Other 
Requires:	%{name} = %{version}-%{release}

%description cli
This package contains simple command line tool for working
with problem dump reports

%files cli
%{_bindir}/report-cli
%{_mandir}/man1/report-cli.1.*

#--------------------------------------------------------------------

%package newt
Summary:	%{name}'s newt interface
Group:		Graphical desktop/Other 
Requires:	%{name} = %{version}-%{release}
Provides:	report-newt = 0.23-1
Obsoletes:	report-newt < 0.23-1

%description newt
This package contains a simple newt application for reporting
bugs

%files newt
%{_bindir}/report-newt
%{_mandir}/man1/report-newt.1.*

#--------------------------------------------------------------------

%package gtk
Summary:	GTK front-end for libreport
Group:		Graphical desktop/GNOME
Requires:	libreport = %{version}-%{release}
Provides:	report-gtk = 0.23-1
Obsoletes:	report-gtk < 0.23-1

%description gtk
Applications for reporting bugs using libreport backend

%files gtk
%{_bindir}/report-gtk
%{_mandir}/man1/report-gtk.1.*

#--------------------------------------------------------------------

%define lib_major_gtk 0
%define libname_gtk %mklibname report-gtk %{lib_major_gtk}

%package -n %{libname_gtk}
Summary:	GTK front-end for libreport
Group:		System/Libraries

%description -n %{libname_gtk}
Applications for reporting bugs using libreport backend

%files -n %{libname_gtk}
%{_libdir}/libreport-gtk.so.%{lib_major_gtk}*

#--------------------------------------------------------------------

%define lib_namegtk_devel %mklibname report-gtk -d

%package -n %{lib_namegtk_devel}
Summary:	Development libraries and headers for libreport
Group:		Development/GNOME and GTK+ 
Requires:	libreport-gtk = %{version}-%{release}
Requires:	%{libname_gtk} = %{version}-%{release}
Provides:	%{name}-gtk-devel = %{version}-%{release}

%description -n %{lib_namegtk_devel}
Development libraries and headers for libreport-gtk

%files -n %{lib_namegtk_devel}
%{_libdir}/libreport-gtk.so
%{_includedir}/libreport/internal_libreport_gtk.h
%{_libdir}/pkgconfig/libreport-gtk.pc

#--------------------------------------------------------------------

%package plugin-kerneloops
Summary:	%{name}'s kerneloops reporter plugin
Group:		System/Libraries
Requires:	curl
Requires:	%{name} = %{version}-%{release}

%description plugin-kerneloops
This package contains plugin which sends kernel crash information to specified
server, usually to kerneloops.org.

%files plugin-kerneloops
%{_datadir}/libreport/events/report_Kerneloops.xml
%{_mandir}/man*/reporter-kerneloops.*
%{_bindir}/reporter-kerneloops

#--------------------------------------------------------------------

%package plugin-logger
Summary:	%{name}'s logger reporter plugin
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-logger < 2.0.4
Provides:	report-plugin-localsave = 0.23-1
Obsoletes:	report-plugin-localsave < 0.23-1
Provides:	report-config-localsave = 0.23-1
Obsoletes:	report-config-localsave < 0.23-1

%description plugin-logger
The simple reporter plugin which writes a report to a specified file.

%files plugin-logger
%{_sysconfdir}/libreport/events/report_Logger.conf
%{_datadir}/libreport/events/report_Logger.xml
%{_datadir}/libreport/workflows/workflow_Logger*.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/print_event.conf
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_logger.conf
%{_bindir}/reporter-print
%{_mandir}/man*/reporter-print.*
%{_mandir}/man*/report_Logger.conf.*
%{_mandir}/man*/print_event.conf.*
%{_mandir}/man*/report_logger.conf.*

#--------------------------------------------------------------------

%package plugin-mailx
Summary:	%{name}'s mailx reporter plugin
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	mailx
Obsoletes:	abrt-plugin-mailx < 2.0.4

%description plugin-mailx
The simple reporter plugin which sends a report via mailx to a specified
email address.

%files plugin-mailx
%{_datadir}/libreport/events/report_Mailx.xml
%config(noreplace) %{_sysconfdir}/libreport/plugins/mailx.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/mailx_event.conf
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_mailx.conf
%{_datadir}/libreport/conf.d/plugins/mailx.conf
%{_datadir}/libreport/workflows/workflow_Mailx*.xml
%{_mandir}/man*/mailx.conf.*
%{_mandir}/man*/mailx_event.conf.*
%{_mandir}/man*/report_mailx.conf.*
%{_mandir}/man*/reporter-mailx.*
%{_bindir}/reporter-mailx

#--------------------------------------------------------------------

%package plugin-bugzilla
Summary:	%{name}'s bugzilla plugin
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-bugzilla < 2.0.4
Provides:	report-plugin-bugzilla = 0.23-1
Obsoletes:	report-plugin-bugzilla < 0.23-1
Provides:	report-config-bugzilla-redhat-com = 0.23-1
Obsoletes:	report-config-bugzilla-redhat-com < 0.23-1

%description plugin-bugzilla
Plugin to report bugs into the bugzilla.

%files plugin-bugzilla
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format_analyzer_libreport.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_format_kernel.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla_formatdup.conf
%{_datadir}/libreport/events/report_Bugzilla.xml
%{_datadir}/libreport/events/watch_Bugzilla.xml
%{_datadir}/libreport/conf.d/plugins/bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/events/report_Bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/bugzilla_event.conf
# FIXME: remove with the old gui
%{_mandir}/man1/reporter-bugzilla.1.*
%{_mandir}/man5/bugzilla.conf.5.*
%{_mandir}/man5/bugzilla_event.conf.5.*
%{_mandir}/man5/bugzilla_format.conf.5.*
%{_mandir}/man5/bugzilla_format_analyzer_libreport.conf.*
%{_mandir}/man5/bugzilla_format_kernel.conf.5.*
%{_mandir}/man5/bugzilla_formatdup.conf.5.*
%{_mandir}/man5/report_Bugzilla.conf.*
%{_bindir}/reporter-bugzilla

#--------------------------------------------------------------------

%package plugin-ureport
Summary: %{name}'s micro report plugin
BuildRequires: json-c-devel
Group: System/Libraries
Requires: %{name} = %{version}-%{release}

%description plugin-ureport
Uploads micro-report to abrt server

%files plugin-ureport
%{_datadir}/libreport/events/report_uReport.xml
%{_bindir}/reporter-ureport
%{_mandir}/man1/reporter-ureport.1.*
%{_mandir}/man5/ureport.conf.5.*
%{_datadir}/libreport/conf.d/plugins/ureport.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/ureport.conf

#--------------------------------------------------------------------

%package compat
Summary:	%{name}'s compat layer for obsoleted 'report' package
Group:		System/Libraries
Requires:	%{name}-plugin-bugzilla

%description compat
Provides 'report' command-line tool.

%files compat
%{_bindir}/report
%{_mandir}/man1/report.1.*

#--------------------------------------------------------------------

%package plugin-reportuploader
Summary:	%{name}'s reportuploader plugin
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	abrt-plugin-reportuploader < 2.0.4
Provides:	report-plugin-ftp = 0.23-1
Obsoletes:	report-plugin-ftp < 0.23-1
Provides:	report-config-ftp = 0.23-1
Obsoletes:	report-config-ftp < 0.23-1
Provides:	report-plugin-scp = 0.23-1
Obsoletes:	report-plugin-scp < 0.23-1
Provides:	report-config-scp = 0.23-1
Obsoletes:	report-config-scp < 0.23-1

%description plugin-reportuploader
Plugin to report bugs into anonymous FTP site associated with ticketing system.

%files plugin-reportuploader
%{_mandir}/man*/reporter-upload.*
%{_mandir}/man*/uploader_event.conf.*
%{_mandir}/man*/report_uploader.conf.*
%{_bindir}/reporter-upload
%{_datadir}/libreport/events/report_Uploader.xml
%{_datadir}/libreport/conf.d/plugins/upload.conf
%{_datadir}/libreport/workflows/workflow_Upload*.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/uploader_event.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/upload.conf
%config(noreplace) %{_sysconfdir}/libreport/workflows.d/report_uploader.conf

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches
#sed -i -e 's!-Werror!-Wno-deprecated!' configure{.ac,} */*/Makefile*
perl -pi -e 's|bugzilla.redhat.com|issues.openmandriva.org|g' src/plugins/report_Bugzilla.xml{,.in} src/plugins/bugzilla.conf

[ -e autogen.sh ] && ./autogen.sh

%define Werror_cflags %nil
#autoreconf -fi
#intltoolize -f

%build
%configure \
%if ! %{with python2}
	--without-python2
%endif

%make CFLAGS="%{optflags} -fno-strict-aliasing" 

%install
%makeinstall_std mandir=%{_mandir}
%find_lang %{name}

mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/events.d/
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/events/

# After everything is installed, remove info dir
rm -f %{buildroot}%{_infodir}/dir

rm -f %{buildroot}%{_sysconfdir}/libreport/plugins/bugzilla_format_anaconda.conf
rm -f %{buildroot}%{_sysconfdir}/libreport/plugins/bugzilla_formatdup_anaconda.conf
rm -f %{buildroot}%{_sysconfdir}/libreport/events.d/bugzilla_anaconda_event.conf
rm -f %{buildroot}%{_sysconfdir}/libreport/plugins/rhtsupport.conf
rm -f %{buildroot}%{_datadir}/libreport/events/report_RHTSupport.xml
rm -f %{buildroot}%{_datadir}/libreport/events/report_EmergencyAnalysis.xml
rm -f %{buildroot}%{_sysconfdir}/libreport/events.d/rhtsupport_event.conf
rm -f %{buildroot}%{_sysconfdir}/libreport/events.d/emergencyanalysis_event.conf
rm -f %{buildroot}%{_mandir}/man1/reporter-rhtsupport.1.*
rm -f %{buildroot}%{_mandir}/man5/anaconda_event.conf*
rm -f %{buildroot}%{_mandir}/man5/bugzilla_anaconda_event.conf*
rm -f %{buildroot}%{_mandir}/man5/bugzilla_format_anaconda.conf*
rm -f %{buildroot}%{_mandir}/man5/bugzilla_formatdup_anaconda.conf*
rm -f %{buildroot}%{_mandir}/man5/emergencyanalysis_event.conf*
rm -f %{buildroot}%{_mandir}/man5/rhtsupport.conf*
rm -f %{buildroot}%{_mandir}/man5/rhtsupport_event.conf*
rm -f %{buildroot}%{_mandir}/man5/report_fedora.conf*
rm -f %{buildroot}%{_mandir}/man5/report_rhel.conf*
rm -f %{buildroot}%{_mandir}/man5/report_rhel_bugzilla.conf*
rm -f %{buildroot}%{_bindir}/reporter-rhtsupport
rm -f %{buildroot}%{_datadir}/dbus-1/interfaces/*rhtsupport*.xml
rm -f %{buildroot}%{_datadir}/libreport/workflows/workflow*{Anaconda,Fedora,RHEL}*.xml
rm -f %{buildroot}%{_sysconfdir}/libreport/workflows.d/anaconda_event.conf
rm -f %{buildroot}%{_sysconfdir}/libreport/workflows.d/report_fedora.conf
rm -f %{buildroot}%{_sysconfdir}/libreport/workflows.d/report_rhel.conf
rm -f %{buildroot}%{_sysconfdir}/libreport/workflows.d/report_rhel_bugzilla.conf
rm -f %{buildroot}%{_datadir}/libreport/conf.d/plugins/rhtsupport.conf
find %{buildroot} -name *rhtsupport* -exec rm {} \;


%if %{_with_tests}
%check
make check
%endif
