Name:           flatbuffers
Version:	%{VERSION}
Release:        1%{?dist}
Summary:        Memory Efficient Serialization Library from Google
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Url:            http://google.github.io/flatbuffers/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3
BuildRequires:  gcc-c++

%description
FlatBuffers is a serialization library for games and other memory constrained apps.
FlatBuffers allows you to directly access serialized data without unpacking/parsing
it first, while still having great forwards/backwards compatibility.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:	%{name} = %{version}

%description    devel
FlatBuffers is a serialization library for games and other memory constrained apps.
FlatBuffers allows you to directly access serialized data without unpacking/parsing
it first, while still having great forwards/backwards compatibility.

%prep
%setup -q
chmod -x LICENSE.txt readme.md

%build
cmake3 . -DFLATBUFFERS_BUILD_SHAREDLIB=ON -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE.txt readme.md
%{_libdir}/libflatbuffers.so*

%files devel
%defattr(-,root,root)
%{_bindir}/flatc
%{_includedir}/flatbuffers
%{_libdir}/libflatbuffers.a
%{_libdir}/cmake/flatbuffers/*.cmake

%changelog

