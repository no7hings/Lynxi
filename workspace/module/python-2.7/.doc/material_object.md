
```mermaid

graph TB

subgraph value
    value("Value")
    value -.-> typed_value("Typed of Value")
end

subgraph port
    port("Port") -.-> shader_input("Shaderinput")
    value --> port
    typed_value --> shader_input
end

subgraph dag
    dag("Dag") -.-> shader("Shader")
    port --> dag
    shader_input --> shader
    
    shader -.-> surface_shader("SurfaceShader")
    shader -.-> displacement_Shader("DisplacementShader")
    shader -.-> volume_shader("VolumeShader")
end

subgraph set
    set("Set") -.-> shader_set("Shaderset")
    dag --> set
    surface_shader --> shader_set
    displacement_Shader --> shader_set
    volume_shader --> shader_set
end

classDef red_0 fill:#f99,stroke:#000,stroke-width:1px,fill-opacity:1
classDef orange_0 fill:#fc9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef yellow_0 fill:#ff9,stroke:#000,stroke-width:1px,fill-opacity:1
classDef green_0 fill:#9fc,stroke:#000,stroke-width:1px,fill-opacity:1
classDef blue_0 fill:#9cf,stroke:#000,stroke-width:1px,fill-opacity:1
classDef violet_0 fill:#ccf,stroke:#000,stroke-width:1px,fill-opacity:1
classDef pink_0 fill:#f9c,stroke:#000,stroke-width:1px,fill-opacity:1
classDef white_0 fill:#fff,stroke:#000,stroke-width:1px,fill-opacity:1

class typed_value red_0
class shader_input red_0
class surface_shader red_0
class shader_set red_0
```

