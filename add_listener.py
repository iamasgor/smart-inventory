import re

# Read the file
with open('products/templates/products/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the location to insert the new event listener (after the productAdded listener)
pattern = r'(      }, 350\);\s+}\);\s+</script>)'

replacement = r'''      }, 350);
    });

    // close bootstrap modal when server triggers 'productUpdated'
    htmx.on("productUpdated", function(evt) {
      const modalEl = document.getElementById('productEditModal');
      const bsModal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
      bsModal.hide();

      // optional: reset the form after a very short timeout (after hide animation)
      setTimeout(() => {
        const form = modalEl.querySelector('form');
        if (form) form.reset();
        // remove any preview images if present
        const preview = modalEl.querySelector('.image-preview');
        if (preview) preview.innerHTML = '';
      }, 350);
    });
    </script>'''

# Replace
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# Write back
with open('products/templates/products/base.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Event listener added successfully!")
