"""Local Sphinx extension to fix sphinx-codeautolink and sphinx-exercise conflict."""

def setup(app):
    try:
        import sphinx_codeautolink.extension.block as block
        
        # Dynamically locate the visitor class and patch its depart_section method
        for name in dir(block):
            obj = getattr(block, name)
            if isinstance(obj, type) and hasattr(obj, 'depart_section'):
                original_depart = obj.depart_section
                
                def safe_depart(self, node, orig=original_depart):
                    try:
                        orig(self, node)
                    except IndexError:
                        # Safely catch the empty stack bug caused by exercise target nodes
                        pass
                
                # Apply the patch
                obj.depart_section = safe_depart
    except ImportError:
        pass

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }