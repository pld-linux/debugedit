#
# Conditional build:
%bcond_without	tests	# build without tests
#
Summary:	Tools for debuginfo creation
Summary(pl.UTF-8):	Narzędzia do tworzenia plików z danymi dla debuggerów
Name:		debugedit
Version:	5.0
Release:	3
License:	GPL v3+, GPL v2+
Group:		Development/Tools
Source0:	https://sourceware.org/ftp/debugedit/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	9961a1ae59b6417d27e3a646dc4078b7
Patch0:		0001-tests-Handle-zero-directory-entry-in-.debug_line-DWA.patch
Patch1:		no-exe-for-elf-debuginfo.patch
URL:		https://sourceware.org/debugedit/
BuildRequires:	autoconf >= 1.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	elfutils-devel
BuildRequires:	help2man
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Debugedit provides programs and scripts for creating debuginfo and
source file distributions, collect build-ids and rewrite source paths
in DWARF data for debugging, tracing and profiling.

%description -l pl.UTF-8
Ten pakiet zawiera programy i skrypty do tworzenia pakietów z plikami
debuginfo i źródłowymi, zbierania build-id oraz przepisywania ścieżek
do źródeł w danych DWARF w celu diagnozowania błędów, śledzenia i
profilowania oprogramowania.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
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
