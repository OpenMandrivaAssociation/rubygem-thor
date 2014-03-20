%define gemname thor
Summary:	A scripting framework that replaces rake, sake and rubigen
Name:		rubygem-%{gemname}
Version:	0.14.6
Release:	4
Source0:	http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1:        %{name}.rpmlintrc
License:	MIT
Group:		System/Servers
Url:		http://www.rubyonrails.org/
BuildRoot:	%{_tmppath}/%{gemname}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems
Provides:       rubygem(%{gemname}) = %{version}

%description
A scripting framework that replaces rake, sake and rubigen.

%prep
%setup -c

%build

%install

gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%defattr(-,root,root)
%{_bindir}/rake2thor
%{_bindir}/thor
%{ruby_gemdir}/gems/%{gemname}-%{version}
%{ruby_gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{gemname}-%{version}


%changelog
* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.14.6-4
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 0.14.6-3
+ Revision: 769823
- Fix file list

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 0.14.6-2
+ Revision: 769795
- Manual provides

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 0.14.6-1
+ Revision: 769794
- New mdv package
- Created package structure for 'rubygem-thor'.

