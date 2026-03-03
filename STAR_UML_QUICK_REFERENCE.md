# ⚡ Star UML - Quick Reference Card
## Fast Visual Guide & Keyboard Shortcuts

---

## 🎯 GETTING STARTED (5 MINUTES)

### Installation
```
1. Visit: https://staruml.io/download
2. Download for your OS (Windows/Mac/Linux)
3. Install and launch
4. Create new UML project: File → New → UML
```

### Initial Setup
```
File → New → UML Project
Project Name: AquaIntel
Location: c:\Users\Rakesh S\Desktop\ccp
Click: Create
```

---

## 🎨 TOOLBAR LOCATION & ICONS

### Main Toolbar (Top of Diagram)

```
┌─────────────────────────────────────────────────┐
│ [Class] [Interface] [Enum] [Datatype]           │
│ [Generalization] [Realization] [Dependency]    │
│ [Association] [Composition] [Aggregation]      │
│ [Note] [Comment] [Constraint]                  │
│ [Multiplicity] [Role] [Visibility]             │
└─────────────────────────────────────────────────┘

CLASS TOOL:
- Icon: Rectangle with 3 compartments
- For: Creating class boxes
- Click then drag on canvas

RELATIONSHIP TOOLS:
- Generalization: Solid line with triangle (inheritance)
- Realization: Dashed line with triangle (interface)
- Dependency: Dashed line with arrow
- Association: Solid line with arrow
- Composition: Solid line with filled diamond
- Aggregation: Solid line with hollow diamond
```

---

## 📝 CREATING A CLASS: STEP-BY-STEP

### Method 1: Toolbar (Recommended for beginners)

```
STEP 1: Click [Class] in toolbar
        (Rectangle icon with 3 sections)

STEP 2: Move cursor to canvas
        (Cursor changes to crosshair)

STEP 3: Click and drag to create class box
        (Draw a rectangle)

STEP 4: Type class name
        (Name appears at top)

STEP 5: Press Enter to confirm
```

### Method 2: Right-click Menu

```
RIGHT-CLICK on canvas
→ Select "Class"
→ Choose type of class
→ Click location
→ Type name
```

### Method 3: Keyboard Shortcut

```
1. Open Element menu → Class
   (Or use keyboard: depends on Star UML version)

2. Type class name directly
```

---

## ⚙️ EDITING CLASS PROPERTIES

### Access Properties Panel (Right side)

```
Your class is selected (highlighted in blue)
↓
Look at Right Panel (Properties)
↓
If not visible: View → Properties Panel → Show
```

### ADD ATTRIBUTES

```
Find "Attributes" section in Properties Panel
├─ Click "+" button
├─ Type attribute name: - models: Dict
├─ Press Enter
├─ Type next: - weights: Dict
├─ Press Enter
└─ Continue...

Format: [visibility] name: type = default_value
Example: - models: Dict<str, Any>
         + trained: bool = False
         # private_var: float
```

### ADD METHODS

```
Find "Operations" section in Properties Panel
├─ Click "+" button
├─ Type method: __init__()
├─ Press Enter
├─ Type next: initialize_models()
├─ Press Enter
└─ Continue...

Format: [visibility] name(parameters): return_type
Example: + predict(lat: float, lon: float): Dict
         - _calculate(x: float): float
```

### Visibility Symbols

```
+ Public (visible everywhere)
- Private (only in this class)
# Protected (this class + children)
~ Package (within same package)

Examples in properties:
+ public_method()
- _private_method()
# protected_method()
```

---

## 🔗 CREATING RELATIONSHIPS

### Method 1: Click Relationship Tool → Draw

```
COMPOSITION (solid line with filled diamond):
1. Click [Composition] tool in toolbar
2. Click on PARENT class
3. Drag to CHILD class
4. Release to create line
5. Small filled diamond appears at child end

Example: AdvancedEnsemblePredictor ◆━━ Model

AGGREGATION (solid line with hollow diamond):
1. Click [Aggregation] tool
2. Click on CONTAINER class
3. Drag to CONTAINED class
4. Release to create line
5. Small hollow diamond appears at contained end

Example: FastAPI ◇━━ Ensemble

DEPENDENCY (dashed line with arrow):
1. Click [Dependency] tool
2. Click on DEPENDENT class
3. Drag to DEPENDENCY class
4. Release to create line
5. Dashed line with arrow appears

Example: RealtimeEngine ╌╌╌► External APIs
```

### Method 2: Using Context Menu

```
RIGHT-CLICK on class
→ Add → Composition/Aggregation/Dependency
→ Then drag end point to target class
```

---

## 🏷️ EDIT RELATIONSHIP PROPERTIES

### Add Labels & Multiplicity

```
Double-click on relationship line
→ Properties panel opens for the relationship

Set:
- Role Name (what it represents)
- Multiplicity at Source End (left)
  └─ 1, *, 0..1, 1..*, etc.
- Multiplicity at Target End (right)
  └─ 1, 5, 10, *, etc.

Example Multiplicities:
┌───────────────────────────────────────┐
│ Source    → (relationship) → Target   │
│ 1         → "contains"    → 5         │
│ (means: 1 parent contains 5 children) │
└───────────────────────────────────────┘
```

### Add Connection Labels

```
1. Double-click relationship line
2. In Properties → Role Name field
3. Type: "uses", "contains", "depends on"
4. Click OK
5. Label appears on line
```

---

## 🎨 FORMAT YOUR DIAGRAM

### Select Multiple Classes

```
Method 1: Click and Drag
└─ Click empty area, drag rectangle over classes

Method 2: Shift + Click
└─ Hold Shift, click each class

Method 3: Ctrl + A
└─ Select all classes in diagram
```

### Apply Formatting

```
Classes selected →
Right-click → Format...
or
Select → Format Menu

Options:
├─ Background Color
│  ├─ Light Blue: #E3F2FD (ML Models)
│  ├─ Light Green: #E8F5E9 (Data Processors)
│  ├─ Light Yellow: #FFFDE7 (API Layer)
│  └─ Light Gray: #EEEEEE (Data Models)
├─ Border Color: Black
├─ Border Width: 2px
├─ Font: Arial, Size 10
└─ Text Color: Black
```

### Align Classes

```
Classes selected →
Right-click → Align

Options:
├─ Align Left
├─ Align Right
├─ Align Top
├─ Align Bottom
├─ Distribute Horizontally
└─ Distribute Vertically

Keyboard: (varies by version, check Format menu)
```

---

## 📊 QUICK CLASS TEMPLATES

### Copy-Paste Structure

```
When creating class quickly, use this format:

ATTRIBUTES:
- property1: Type1
- property2: Type2
- property_list: List<Type>
- property_dict: Dict<key, value>

METHODS:
+ __init__(): void
+ method1(param1: Type1): ReturnType
+ method2(param2: Type2): ReturnType
- _private_method(): ReturnType
```

---

## 📋 CREATING OTHER DIAGRAM TYPES

### Sequence Diagram Setup

```
1. Model → Add Diagram → Sequence Diagram
2. Name: "Sequence - [Purpose]"

Add Actors:
- Toolbar: [Actor] tool (stick figure)
- Click to add participants across top

Add Messages:
- Toolbar: [Sync Message] tool (arrow)
- Click from one participant → another
- Type message text

Add Parallel Execution:
- Toolbar: [Alt] or [Par] for frames
- Draw rectangle around parallel steps
- Label: "par [Parallel Execution]"
```

### Component Diagram Setup

```
1. Model → Add Diagram → Component Diagram
2. Name: "Component - [Purpose]"

Add Components:
- Toolbar: [Component] tool (box with circles)
- Creates component representation

Add Connections:
- Use dependency/association arrows
- Connect components with relationships
- Label connections

Add Ports/Interfaces:
- Right-click component → Add Port
- Creates provided/required interfaces
```

### Use Case Diagram Setup

```
1. Model → Add Diagram → Use Case Diagram
2. Name: "UseCase - [Purpose]"

Add Actors:
- Toolbar: [Actor] tool

Add UseCases:
- Toolbar: [UseCase] tool (oval)

Add Relationships:
- [Association] arrow from actor to use case
- [Include] for "include another use case"
- [Extend] for "conditional use case"

Example:
User ━━━> Make Prediction (use case)
```

### Deployment Diagram Setup

```
1. Model → Add Diagram → Deployment Diagram
2. Name: "Deployment - [Purpose]"

Add Nodes:
- Toolbar: [Node] tool (3D cube)
- Represents hardware/servers

Add Artifacts:
- Right-click Node → Add Artifact
- Represents deployed software

Add Connections:
- [Dependency] arrow between nodes
- Shows deployment relationships
```

---

## 💾 SAVING & EXPORTING

### Save Project

```
File → Save        [Ctrl+S]
─ Saves as .mdj file (Star UML format)

File → Save As     [Ctrl+Shift+S]
─ Choose new location/name

Auto-save is enabled by:
File → Preferences → General → Auto Save
```

### Export Single Diagram

```
File → Export      [Ctrl+E]
├─ Select format:
│  ├─ PNG (best for presentations) - 300 DPI
│  ├─ PDF (for reports)
│  ├─ SVG (for web/editing)
│  └─ EPS (for printing)
├─ Choose output folder
└─ Click Export
```

### Export All Diagrams

```
File → Export Diagrams
├─ Select all diagrams to export
├─ Choose format
├─ Choose output folder
└─ Click Export All

Creates:
├─ ClassDiagram.png
├─ SequenceDiagram.png
├─ ComponentDiagram.png
└─ ... (all selected diagrams)
```

### Export as XMI (Backup Format)

```
File → Export As... (or right-click project)
├─ Choose XMI format
├─ Can import in other UML tools
└─ Good for version control
```

---

## ⌨️ ESSENTIAL KEYBOARD SHORTCUTS

### File Operations
```
Ctrl+N: New Project
Ctrl+O: Open Project
Ctrl+S: Save
Ctrl+Shift+S: Save As
Ctrl+E: Export
Ctrl+W: Close Diagram
Ctrl+Q: Quit
```

### Editing
```
Ctrl+Z: Undo
Ctrl+Y: Redo
Ctrl+C: Copy
Ctrl+X: Cut
Ctrl+V: Paste
Delete: Delete selected
Ctrl+A: Select All
Escape: Deselect All
```

### Diagram Navigation
```
Ctrl++: Zoom In
Ctrl+-: Zoom Out
Ctrl+0: Fit to Window
Ctrl+1: 100% Zoom
Ctrl+2: 200% Zoom
Space + Drag: Pan view
Mouse Wheel: Zoom
```

### View Options
```
Ctrl+F1: Show Diagrams
Ctrl+F2: Show Properties
Ctrl+F3: Show Model
Ctrl+F4: Show Preview
F5: Refresh View
```

---

## 🎯 COMMON TASKS QUICK REFERENCE

### Rename a Class
```
1. Select class (click on it)
2. Press F2 (or double-click name)
3. Type new name
4. Press Enter
```

### Change Class Type
```
1. Select class
2. Right-click → Type
3. Choose: Class, Interface, Abstract, Enum, etc.
4. Click OK
```

### Add Stereotype
```
1. Select class
2. Right-click → Edit Stereotype
3. Type: DataModel, Concrete, Abstract, etc.
4. Click OK
Note: Appears in << >> on diagram
```

### Add Comment
```
1. Toolbar: [Note] tool (yellow rectangle)
2. Click on diagram to place note
3. Type comment text
4. Optional: draw line to class

Comment Box shows documentation/explanation
```

### Add Constraint
```
1. Toolbar: [Constraint] tool (curly braces)
2. Click on diagram
3. Type constraint: {realization of IPredictor}
4. Connect to relevant class if needed
```

---

## 🎨 RECOMMENDED DIAGRAM LAYOUT

### For Class Diagram

```
Position classes in layers:

TOP LAYER: API/Controller
        ┌─────────────────┐
        │  FastAPI_App    │
        └─────────────────┘

MIDDLE LAYER: AI/ML Engines
  ┌──────────┬──────────┬──────────┐
  │ Ensemble │Transform │  LSTM    │
  └──────────┴──────────┴──────────┘

LOWER MIDDLE: Data Processors
  ┌──────────┬──────────┬──────────┐
  │Satellite │Geospatial│ RealTime │
  └──────────┴──────────┴──────────┘

BOTTOM LAYER: Supporting Classes
  ┌──────────────────────────────────┐
  │  Pydantic Models & Data Types    │
  └──────────────────────────────────┘

LEFT SIDE: External APIs (as notes)
RIGHT SIDE: Legend/Info boxes
```

---

## ❌ COMMON MISTAKES TO AVOID

```
❌ Creating one giant diagram with everything
✅ Split into focused diagrams (by concern)

❌ Too many overlapping relationships
✅ Use multiple diagrams for clarity

❌ Forgetting multiplicity labels
✅ Always label: 1, *, 0..*, etc.

❌ No stereotypes or colors
✅ Use <<DataModel>>, <<Concrete>>, colors

❌ Wrong relationship type used
✅ Composition (◆) = contains
   Aggregation (◇) = uses
   Dependency (╌╌╌►) = temporary

❌ Methods and attributes too detailed
✅ Show only important ones
   (Hide getters/setters if not relevant)

❌ Not saving project files
✅ Save as .mdj (Star UML native)
   Export as .xml (XMI backup)
   Export as .png (for sharing)
```

---

## 🚀 WORKFLOW FOR FAST DIAGRAM CREATION

### 30-Minute Fast Diagram

```
STEP 1 (5 min): Create project
└─ New UML Project → Basic setup

STEP 2 (10 min): Create 5 main classes
└─ Quickly add boxes, basic names

STEP 3 (10 min): Add attributes & methods
└─ Add 3-5 key attributes
└─ Add 5-10 key methods

STEP 4 (5 min): Add relationships
└─ Draw composition/aggregation lines
└─ Add multiplicity labels

RESULT: Basic diagram showing main classes & relationships
```

### 2-Hour Complete Diagram

```
STEP 1 (15 min): Create all 8 core classes
STEP 2 (20 min): Add all attributes & methods
STEP 3 (20 min): Add all relationships
STEP 4 (15 min): Format & color code
STEP 5 (15 min): Add notes & documentation
STEP 6 (10 min): Export & save
STEP 7 (5 min): Review & verify

RESULT: Professional class diagram ready for presentation
```

---

## 📌 CHECKLISTS FOR EACH DIAGRAM TYPE

### Class Diagram Checklist
```
─ All main classes created
─ All attributes added with types
─ All methods added with signatures
─ Relationships drawn correctly
─ Multiplicity labels added
─ Color coding applied
─ Stereotypes added where needed
─ Arranged in logical layout
─ Comments added for complex areas
─ Exported and saved
```

### Sequence Diagram Checklist
```
─ All participants/actors added
─ Message calls in correct order
─ Parallel execution shown with par frame
─ Alt/if blocks for conditionals
─ Return messages shown (dashed)
─ Activation boxes shown
─ Multiplicity shown where needed
─ All steps documented
─ Export at high resolution
```

### Component Diagram Checklist
```
─ All components created
─ Connections between components shown
─ Interfaces/ports displayed
─ Provided interfaces marked
─ Required interfaces marked
─ Dependencies clear
─ Legend/notes added
─ Export ready
```

---

## 🎓 WHERE TO FIND THINGS IN STAR UML

| Task | Location | Shortcut |
|------|----------|----------|
| Create Class | Toolbar → Class Icon | - |
| Add Attribute | Properties Panel → Attributes → + | - |
| Add Method | Properties Panel → Operations → + | - |
| Create Relationship | Toolbar → Relationship Tools | - |
| Format Class | Right-click → Format | - |
| Save Project | File → Save | Ctrl+S |
| Export | File → Export | Ctrl+E |
| Properties Panel | View → Properties | Ctrl+F2 |
| Model Explorer | View → Model | Ctrl+F1 |
| Undo | Edit → Undo | Ctrl+Z |
| Redo | Edit → Redo | Ctrl+Y |
| Delete | Select + Delete key | Delete |
| Zoom In | View → Zoom → In | Ctrl++ |
| Zoom Out | View → Zoom → Out | Ctrl+- |

---

## 💡 PRO TIPS

```
TIP 1: Use templates
└─ Create one class completely, then copy/paste
└─ Saves time on attribute/method entry

TIP 2: Use layers
└─ Organize classes in logical layers
└─ Easier to understand architecture

TIP 3: Add documentation as you go
└─ Comments and notes before you forget
└─ Makes diagrams more maintainable

TIP 4: Color code by function
└─ Immediate visual understanding
└─ Share consistent colors across project

TIP 5: Create multiple focused diagrams
└─ One complex diagram → 2-3 simpler ones
└─ Each focuses on specific concern

TIP 6: Use Export for presentations
└─ PNG at 300 DPI for high quality
└─ 1920x1080 resolution recommended

TIP 7: Backup your work
└─ Save as both .mdj (native) and .xml (XMI)
└─ Can be imported in other UML tools

TIP 8: Review relationships regularly
└─ Makes sure all connections make sense
└─ Catch errors early
```

---

## 📱 STAR UML INTERFACE OVERVIEW

```
┌─────────────────────────────────────────────────────────┐
│  File Edit View Format Tools Window Help               │
├────────────────────────────────────────────────────────┤
│ [Toolbar with Class, Relationship, Shape tools]       │
├────────────^─────────────────────────────────────────┤
│  │                                          │          │
│  │    MODEL EXPLORER               │ PROPERTIES         │
│  │  • Project                      │ • Name             │
│  │    ├─ ClassDiagram1             │ • Type             │
│  │    ├─ Sequence1                 │ • Visibility       │
│  │    └─ Component1                │ • Attributes       │
│  │                                  │ • Operations       │
│  │                                  │ • Relationships    │
│  │                                  │ • Constraints      │
│  │                                  │ • Tags             │
│  │        CANVAS AREA              │ • Custom           │
│  │  (Drag classes, draw            │                    │
│  │   relationships here)            │                    │
│  │                                  │                    │
│  └─────────────────────────────────┴──────────────────┘
└───────────────────────────────────────────────────────┘

LEFT PANEL: Model Explorer (view project structure)
CENTER: Canvas (drawing area)
RIGHT PANEL: Properties (edit selected element)
```

---

**You now have everything to create professional UML diagrams in Star UML!** 🎉

**Start with:** Creating your first class
**Next:** Add relationships between classes
**Then:** Export and create other diagram types
**Finally:** Polish and document

**Total Time to Mastery:** 2-3 hours of practice

