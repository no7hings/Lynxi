# Definition

## Resource

### Module

```mermaid
graph LR

basic("Basic") -->|"inherit"| path
    path -->|"inherit"| root
    path -->|"inherit"| directory

basic -->|"inherit"| bin("Bin")
    bin -->|"inherit"| language("Language")
    bin -->|"inherit"| platform("Platform")
    bin -->|"inherit"| application("Application")
        platform --- application
        language --- application
        
basic --- config("Config")
    config --- resource_config("ResourceConfig")
        resource_config -->|"inherit"| application_config("Cfg_WinApplication")
        resource_config -->|"inherit"| module_app_plug("Cfg_WinAppPlug")
        
        resource_config -->|"inherit"| package_config("Cfg_WinPythonPackage")
        resource_config -->|"inherit"| package_app_config("Cfg_WinAppPythonPackage")
        
        resource_config -->|"inherit"| module_config("Cfg_WinPythonModule")
        resource_config -->|"inherit"| module_app_config("Cfg_WinAppPythonModule")
        
        resource_config -->|"inherit"| scheme_config("Cfg_WinPythonScheme")
        resource_config -->|"inherit"| scheme_app_config("Cfg_WinAppPythonScheme")
```

### Raw

- graph

```mermaid
graph RL

resource(("resource"))
    resource_enable("enable = bool")  --- resource
    resource_category("category = str") --- resource
    resource_name("name = str") --- resource

application("application") === resource
    application_name("name = str") --- application
    application_version("version = str") --- application
    
    application_platform("platform") === application
        platform_name("name = str") --- application_platform
        platform_version("version = str") --- application_platform
    
    application_language("language") === application
        language_name("name = str") --- application_language
        language_version("version = str") --- application_language

version("version") === resource
    version_record("record = list") --- version
        record_version("str") --- version_record
    version_active("active = str") --- version

environ("environ") === resource
    environ_key("str(environ_key)") === environ
        environ_value("value = str/list") --- environ_key
        environ_operate("operate = str") --- environ_key

dependent("dependent") === resource
    dependent_category("str(resource_category)") === dependent
        dependent_name("str(resource_name)") === dependent_category
            dependent_version("version = str") --- dependent_name
            dependent_argument("argument = str/list") --- dependent_name
            


classDef pink_0 fill:#f9c,stroke:#000,stroke-width:1px,fill-opacity:1
classDef pink_1 fill:#f59,stroke:#000,stroke-width:1px,fill-opacity:1
classDef red_0 fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef red_1 fill:#f55,stroke:#000,stroke-width:1px,fill-opacity:1
classDef orange_0 fill:#fc9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef orange_1 fill:#f95,stroke:#000,stroke-width:1px,fill-opacity:1
classDef violet_0 fill:#ccf,stroke:#000,stroke-width:1px,fill-opacity:1
classDef violet_1 fill:#99f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef yellow_0 fill:#ff9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef yellow_1 fill:#ff5,stroke:#000,stroke-width:1px,fill-opacity:1
classDef blue_0 fill:#9cf,stroke:#000,stroke-width:1px,fill-opacity:1
classDef blue_1 fill:#59f,stroke:#000,stroke-width:1px,fill-opacity:1
classDef green_0 fill:#9fc,stroke:#000,stroke-width:1px,fill-opacity:1
classDef green_1 fill:#5f9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef white_0 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

class resource orange_0
class application orange_0
class version orange_0
class environ orange_0
class dependent orange_0
class application_platform orange_0
class application_language orange_0
```

- json

```json
{
    "enable": true, 
    "category": "windows_python_module", 
    "name": "LxWindows", 
    "application": {
        "name": "python", 
        "version": "2.7.x", 
        "application": {
            "version": "share", 
            "name": "windows"
        }, 
        "language": {
            "version": "2.7.x", 
            "name": "python"
        }
    }, 
    "environ": {
        "PATH": {
            "operate": "+", 
            "value": "{sourcepath}"
        }
    }, 
    "dependent": {
        "windows_bin": {
            "python": {
                "argument": "share"
            }
        }, 
        "windows_python_module": {
            "LxInterface": {
                "version": "active", 
                "argument": "2.7.x"
            }, 
            "LxUi": {
                "version": "active", 
                "argument": "2.7.x"
            }, 
            "LxCore": {
                "version": "active", 
                "argument": "2.7.x"
            }
        }
    }, 
    "version": {
        "active": "0.0.0", 
        "record": [
            "0.0.0"
        ]
    }
}
```
