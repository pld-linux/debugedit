#
# Conditional build:
%bcond_without	tests		# build without tests
#
Summary:	Tools for debuginfo creation
Name:		debugedit
Version:	5.0
Release:	1
License:	GPL v2/LGPL
Group:		Applications
Source0:	https://sourceware.org/ftp/debugedit/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	9961a1ae59b6417d27e3a646dc4078b7
Patch0:		0001-tests-Handle-zero-directory-entry-in-.debug_line-DWA.patch
URL:		https://sourceware.org/debugedit/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	elfutils-devel
BuildRequires:	help2man
Requires:	awk
Requires:	binutils
Requires:	coreutils
Requires:	dwz
Requires:	elfutils
Requires:	findutils
Requires:	grep
Requires:	sed
Requires:	xz
Suggests:	gdb
#Provides:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Debugedit provides programs and scripts for creating debuginfo and
source file distributions, collect build-ids and rewrite source paths
in DWARF data for debugging, tracing and profiling.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/debugedit
%attr(755,root,root) %{_bindir}/find-debuginfo
%attr(755,root,root) %{_bindir}/sepdebugcrcfix
%{_mandir}/man1/debugedit.1*
%{_mandir}/man1/find-debuginfo.1*
%{_mandir}/man1/sepdebugcrcfix.1*
