Name:       c-b20-515-14
Version:    1.0
Release:    1%{?dist}
Summary:    Программа студента Соколовский Степан группы Б20-515
Group:      Testing
License:    GPL
URL:        https://github.com/StephanSok
Source:     %{name}-%{version}.tar.gz
BuildRequires: gcc

%global debug_package %{nil}

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-b20-515-14 c-b20-515-14.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-b20-515-14 %{buildroot}%{_bindir}
sudo rpm -i ~/rpmbuild/RPMS/noarch/b20-515-14-1.0-1.el8.noarch.rpm --force

%files
%{_bindir}/c-b20-515-14

%changelog
* Thu Oct 16 2012 Sokolovskii
- Added %{_bindir}/c-b20-515-14

c-b20-515-14
