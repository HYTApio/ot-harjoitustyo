```mermaid
 classDiagram
      Pieces "*" --> "1" Shapes
      Gameloop "*" --> "1" Grid
      Gameloop "*" --> "1" Pieces
      
      class Shapes{
      }
      
      class Pieces{
      }
      
      class Gameloop{
      }
      
      class Grid{
      }
```
