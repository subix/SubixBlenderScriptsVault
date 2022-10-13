bl_info = {
    "name" : "Object Adder",
    "author" : "Max Michalski",
    "version" : (1, 0),
    "blender" : (3, 1, 2),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh",
}

import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Object Adder"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'NewTab'
    
    def draw(self, context):
        layout = self.layout
        layout.scale_y = 1.4
        
        row = layout.row()
        row.label(text = "Select any option below:")
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon = 'CUBE')
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon = 'SPHERE')
        row = layout.row()
        row.operator("object.text_add", icon = 'FILE_FONT')
        
class PanelA(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'NewTab'
    bl_parent_id = 'PT_TestPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        layout.scale_y = 1.4
        
        row = layout.row()
        row.label(text = "Select an option to scale your object:")
        row = layout.row()
        row.operator("transform.resize")
        row = layout.row()
        col = layout.column()
        col.prop(obj, "scale")
        
class PanelB(bpy.types.Panel):
    bl_label = "Specials"
    bl_idname = "PT_PanelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'NewTab'
    bl_parent_id = 'PT_TestPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Select a Special Option:")
        row = layout.row()
        row.operator("object.shade_smooth", icon = 'MOD_SMOOTH', text = "Set Smooth Shading")
        row = layout.row()
        row.operator("object.subdivision_set")
        row = layout.row()
        row.operator("object.modifier_add")
        
def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)  
    bpy.utils.register_class(PanelB)   
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)
    
if __name__ == "__main__":
    register() 