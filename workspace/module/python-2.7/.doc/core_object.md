[TOC]
# Definition

### Structure

```mermaid
graph LR

develop("Develop Path")
product("Product Path")

server("Server Path")
local("Local Path")
```

## Resource

### Abstract

```mermaid
graph LR

builtin_object("__builtin__.object") -->|"<p><span style='color:#f00;'>inherit</span></p>"| basic("Basic")

    basic -->|"<p><span style='color:#f00;'>inherit</span></p>"| path("Abc_Path")
        path -->|"<p><span style='color:#f00;'>inherit</span></p>"| root("Abc_Root")
        path -->|"<p><span style='color:#f00;'>inherit</span></p>"| dirctory("Abc_Directory")

    
    basic -->|"<p><span style='text-align:left;color:#f00;'>inherit</span></p>"| object("Abc_Object")
        object -->|"<p><span style='color:#f00;'>inherit</span></p>"| system("Abc_System")
    
        object -->|"<p><span style='color:#f00;'>inherit</span></p>"| resource("Abc_Resource")
   
    basic -->|"<p><span style='color:#f00;'>inherit</span></p>"| file("Abc_File")

    basic -->|"<p><span style='color:#f00;'>inherit</span></p>"| raw("Abc_Raw")
        raw -->|"<p><span style='color:#f00;'>inherit</span></p>"| raw_configure("Abc_RawConfigure")
    
    basic -->|"<p><span style='color:#f00;'>inherit</span></p>"| operate("Abc_Operate")
```

### Relation

```mermaid
graph LR

raw_version("RawVAR_kit__window__version") -->|"<p><span style='color:#f00;'>VERSION_CLS</span></p>"| raw_cofigure("Raw_Configure")
raw_environ("Raw_Environ") -->|"<p><span style='color:#f00;'>ENVIRON_CLS</span></p>"| raw_cofigure
raw_dependent("Raw_Dependent") -->|"<p><span style='color:#f00;'>DEPENDENT_CLS</span></p>"| raw_cofigure

pth_root("Pth_Root") -->|"<p><span style='color:#f00;'>ROOT_CLS</span></p>"| pth_directory("Pth_Directory")
pth_directory -->|"<p><span style='color:#f00;'>DIRECTORY_CLS</span></p>"| file("File")
file -->|"<p><span style='color:#f00;'>FILE_CLS</span></p>"| resource("Resource")
raw_cofigure -->|"<p><span style='color:#f00;'>RAW_CLS</span></p>"| resource

sys_platform("Sys_Pltform") -->|"<p><span style='color:#f00;'>SYSTEM_CLS</span></p>"| sys_plt_language("Sys_PltLanguage")
sys_platform -->|"<p><span style='color:#f00;'>SYSTEM_CLS</span></p>"| sys_plt_application("Sys_PltApplication")

sys_plt_application -->|"<p><span style='color:#f00;'>SYSTEM_CLS</span></p>"| sys_plt_app_language("Sys_PltAppLanguage")

branch_1(("or"))

sys_platform --- branch_1
sys_plt_language --- branch_1
sys_plt_application --- branch_1
sys_plt_app_language --- branch_1

branch_1 -->|"<p><span style='color:#f00;'>SYSTEM_CLS</span></p>"| resource

classDef red_0 fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef orange_0 fill:#fc9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef yellow_0 fill:#ff9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef green_0 fill:#9fc,stroke:#000,stroke-width:1px,fill-opacity:1
classDef blue_0 fill:#9cf,stroke:#000,stroke-width:1px,fill-opacity:1
classDef violet_0 fill:#ccf,stroke:#000,stroke-width:1px,fill-opacity:1
classDef pink_0 fill:#f9c,stroke:#000,stroke-width:1px,fill-opacity:1
classDef white_0 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

class resource red_0

class sys_platform orange_0; class sys_plt_language orange_0; class sys_plt_application orange_0; class sys_plt_app_language orange_0

class raw_version green_0; class raw_environ green_0; class raw_dependent green_0; class raw_cofigure green_0

class file blue_0

class pth_root violet_0; class pth_directory violet_0
```

### Configure

- graph

```mermaid
graph RL

configure("configure = dict")
    resource_enable("enable = bool")  --- configure
    resource_typepath("category = str") --- configure
    resource_name("name = str") --- configure

system("system = dict") === configure
    sys_category("category = str") --- system
    sys_name("name = str") --- system
    sys_version("version = str") --- system
    sys_platform("platfrom = dict") --- system

version("version = dict") === configure
    version_record("record = list") --- version
        record_version("str") --- version_record
    version_active("active = str") --- version

environ("environ = dict") === configure
    environ_key("str(environ_key)") === environ
        environ_value("value = str/list") --- environ_key
        environ_operate("operate = str") --- environ_key

dependent("dependent = dict") === configure
    dependent_category("str(resource_typepath)") === dependent
        dependent_name("str(resource_name)") === dependent_category
            dependent_version("version = str") --- dependent_name
            dependent_argument("argument = str/list") --- dependent_name

```

- json

```json
{
    "enable": true, 
    "category": "plt_app_lng_module", 
    "name": "LxMaya", 
    "system": {
        "category": "plt_app_language", 
        "name": "python", 
        "version": "2.7", 
        "platform": {
            "name": "windows", 
            "version": "share"
        }, 
        "application": {
            "name": "maya", 
            "version": "share"
        }
    }, 
    "version": {
        "active": "0.0.0", 
        "record": [
            "0.0.0"
        ]
    }, 
    "environ": {
        "PATH": {
            "operate": "+", 
            "value": "{path.sourcepath}"
        }
    }, 
    "dependent": {
        "plt_lng_module": {
            "LxDatabase": {
                "version": "active", 
                "argument": [
                    "{system.platform.name}", 
                    "{system.platform.version}", 
                    "{system.name}", 
                    "{system.version}"
                ]
            }, 
            "LxDeadline": {
                "version": "active", 
                "argument": [
                    "{system.platform.name}", 
                    "{system.platform.version}", 
                    "{system.name}", 
                    "{system.version}"
                ]
            }, 
            "LxKit": {
                "version": "active", 
                "argument": [
                    "{system.platform.name}", 
                    "{system.platform.version}", 
                    "{system.name}", 
                    "{system.version}"
                ]
            }, 
            "LxGui": {
                "version": "active", 
                "argument": [
                    "{system.platform.name}", 
                    "{system.platform.version}", 
                    "{system.name}", 
                    "{system.version}"
                ]
            }, 
            "LxCore": {
                "version": "active", 
                "argument": [
                    "{system.platform.name}", 
                    "{system.platform.version}", 
                    "{system.name}", 
                    "{system.version}"
                ]
            }
        }
    }
}
```
