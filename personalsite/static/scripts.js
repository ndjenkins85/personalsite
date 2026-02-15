// Modern vanilla JavaScript - no jQuery needed

// Toggle visibility of element
function togglehide(elemId) {
  const elem = document.getElementById(elemId);
  if (!elem) return;
  
  elem.style.display = elem.style.display === 'none' ? 'block' : 'none';
}

// Smooth scroll to anchor (for Projects link)
document.addEventListener('DOMContentLoaded', () => {
  const links = document.querySelectorAll('a[href^="#"]');
  
  links.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href === '#') return;
      
      e.preventDefault();
      const target = document.querySelector(href);
      
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
});

// Gallery: Simple image lazy loading hint
if ('loading' in HTMLImageElement.prototype) {
  const images = document.querySelectorAll('img.lazy');
  images.forEach(img => {
    img.src = img.dataset.src;
  });
}

// Advanced Tag Visualization - Physics-based Force Simulation
document.addEventListener('DOMContentLoaded', () => {
  const canvas = document.getElementById('tag-canvas');
  if (!canvas || typeof tagData === 'undefined') return;
  
  const container = document.getElementById('tag-visualization');
  const rect = container.getBoundingClientRect();
  
  canvas.width = rect.width;
  canvas.height = 500;
  
  const ctx = canvas.getContext('2d');
  let width = canvas.width;
  let height = canvas.height;
  
  // Physics parameters
  const physics = {
    centerForce: 0.015,
    repelForce: 800,
    linkStrength: 0.02,
    linkDistance: 100,
    damping: 0.88,
    minRadius: 12,
    maxRadius: 45,
    dragDamping: 0.3
  };
  
  const maxCount = Math.max(...tagData.nodes.map(n => n.count), 1);
  
  // Initialize nodes with safe positions
  const nodes = tagData.nodes.map(n => {
    const logScale = Math.log(n.count + 1) / Math.log(maxCount + 1);
    const radius = physics.minRadius + logScale * (physics.maxRadius - physics.minRadius);
    
    return {
      id: n.id,
      count: n.count,
      radius: isFinite(radius) ? radius : physics.minRadius,
      x: width / 2 + (Math.random() - 0.5) * width * 0.3,
      y: height / 2 + (Math.random() - 0.5) * height * 0.3,
      vx: 0,
      vy: 0,
      fx: null,
      fy: null,
      hovered: false,
      highlighted: false,
      opacity: 1.0
    };
  });
  
  const links = tagData.links;
  const maxWeight = Math.max(...links.map(l => l.weight), 1);
  
  // Build adjacency map
  const adjacency = new Map();
  nodes.forEach(n => adjacency.set(n.id, new Set()));
  links.forEach(link => {
    if (adjacency.has(link.source) && adjacency.has(link.target)) {
      adjacency.get(link.source).add(link.target);
      adjacency.get(link.target).add(link.source);
    }
  });
  
  const nodeMap = new Map(nodes.map(n => [n.id, n]));
  
  let mouseX = 0, mouseY = 0;
  let hoveredNode = null, draggedNode = null, isDragging = false;
  let dragStartX = 0, dragStartY = 0, didDrag = false;
  
  // Clamp helper to prevent NaN/Infinity
  function clamp(val, min, max) {
    if (!isFinite(val)) return (min + max) / 2;
    return Math.max(min, Math.min(max, val));
  }
  
  function updateHover(x, y) {
    hoveredNode = null;
    for (const node of nodes) {
      const dx = x - node.x;
      const dy = y - node.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      node.hovered = dist < node.radius + 5;
      if (node.hovered) hoveredNode = node;
    }
    
    if (hoveredNode) {
      const connectedIds = adjacency.get(hoveredNode.id);
      nodes.forEach(n => {
        n.highlighted = (n === hoveredNode) || (connectedIds && connectedIds.has(n.id));
        n.opacity = n.highlighted ? 1.0 : 0.3;
      });
    } else {
      nodes.forEach(n => {
        n.highlighted = false;
        n.opacity = 1.0;
      });
    }
  }
  
  // Mouse events
  canvas.addEventListener('mousemove', (e) => {
    const r = canvas.getBoundingClientRect();
    mouseX = e.clientX - r.left;
    mouseY = e.clientY - r.top;
    
    if (isDragging && draggedNode) {
      draggedNode.fx = mouseX;
      draggedNode.fy = mouseY;
      draggedNode.vx = 0;
      draggedNode.vy = 0;
      // Track if we actually moved (not just a click)
      const dist = Math.sqrt((mouseX - dragStartX) ** 2 + (mouseY - dragStartY) ** 2);
      if (dist > 5) didDrag = true;
    } else {
      updateHover(mouseX, mouseY);
    }
    canvas.style.cursor = (hoveredNode || isDragging) ? 'pointer' : 'default';
  });
  
  canvas.addEventListener('mousedown', (e) => {
    if (hoveredNode) {
      isDragging = true;
      didDrag = false;
      draggedNode = hoveredNode;
      dragStartX = mouseX;
      dragStartY = mouseY;
      draggedNode.fx = mouseX;
      draggedNode.fy = mouseY;
      e.preventDefault();
    }
  });
  
  canvas.addEventListener('mouseup', () => {
    if (draggedNode) {
      draggedNode.fx = null;
      draggedNode.fy = null;
    }
    isDragging = false;
    draggedNode = null;
  });
  
  canvas.addEventListener('mouseleave', () => {
    if (draggedNode) {
      draggedNode.fx = null;
      draggedNode.fy = null;
    }
    isDragging = false;
    draggedNode = null;
    updateHover(-1000, -1000);
  });
  
  canvas.addEventListener('click', (e) => {
    if (!didDrag && hoveredNode) {
      window.location.href = `/articles/?tags=${hoveredNode.id}`;
    }
  });
  
  // Physics simulation with NaN guards
  function simulate() {
    for (const node of nodes) {
      if (node.fx !== null && node.fy !== null) {
        node.x = node.fx;
        node.y = node.fy;
        node.vx *= physics.dragDamping;
        node.vy *= physics.dragDamping;
        continue;
      }
      
      // Center gravity
      node.vx += (width / 2 - node.x) * physics.centerForce;
      node.vy += (height / 2 - node.y) * physics.centerForce;
      
      // Node repulsion
      for (const other of nodes) {
        if (node === other) continue;
        const dx = node.x - other.x;
        const dy = node.y - other.y;
        const distSq = dx * dx + dy * dy + 1; // +1 prevents division by zero
        const dist = Math.sqrt(distSq);
        const force = physics.repelForce * (node.radius + other.radius) / distSq;
        
        node.vx += (dx / dist) * force;
        node.vy += (dy / dist) * force;
      }
    }
    
    // Link spring forces
    for (const link of links) {
      const source = nodeMap.get(link.source);
      const target = nodeMap.get(link.target);
      if (!source || !target) continue;
      
      const dx = target.x - source.x;
      const dy = target.y - source.y;
      const dist = Math.sqrt(dx * dx + dy * dy) + 1;
      const idealDist = physics.linkDistance * (1 - link.weight / maxWeight * 0.3);
      const force = (dist - idealDist) * physics.linkStrength * Math.sqrt(link.weight);
      const fx = (dx / dist) * force;
      const fy = (dy / dist) * force;
      
      if (source.fx === null) { source.vx += fx; source.vy += fy; }
      if (target.fx === null) { target.vx -= fx; target.vy -= fy; }
    }
    
    // Update positions
    const margin = 5;
    for (const node of nodes) {
      if (node.fx !== null && node.fy !== null) continue;
      
      node.vx *= physics.damping;
      node.vy *= physics.damping;
      
      // Clamp velocities to prevent explosion
      node.vx = clamp(node.vx, -50, 50);
      node.vy = clamp(node.vy, -50, 50);
      
      node.x += node.vx;
      node.y += node.vy;
      
      // Clamp positions
      node.x = clamp(node.x, node.radius + margin, width - node.radius - margin);
      node.y = clamp(node.y, node.radius + margin, height - node.radius - margin);
    }
  }
  
  // Safe gradient helper
  function safeRadialGradient(x, y, r, color1, color2) {
    x = clamp(x, 0, width);
    y = clamp(y, 0, height);
    r = Math.max(1, isFinite(r) ? r : 10);
    try {
      const g = ctx.createRadialGradient(x, y, 0, x, y, r);
      g.addColorStop(0, color1);
      g.addColorStop(1, color2);
      return g;
    } catch (e) {
      return color1;
    }
  }
  
  function render() {
    ctx.clearRect(0, 0, width, height);
    
    // Draw links
    for (const link of links) {
      const source = nodeMap.get(link.source);
      const target = nodeMap.get(link.target);
      if (!source || !target) continue;
      
      const isHighlighted = source.highlighted && target.highlighted;
      const thickness = 0.5 + Math.log(link.weight + 1) * 1.5;
      
      ctx.beginPath();
      ctx.moveTo(source.x, source.y);
      ctx.lineTo(target.x, target.y);
      
      if (isHighlighted) {
        ctx.strokeStyle = 'rgba(59, 130, 246, 0.6)';
        ctx.lineWidth = thickness * 1.5;
      } else {
        ctx.strokeStyle = `rgba(100, 100, 100, ${0.15 * source.opacity * target.opacity})`;
        ctx.lineWidth = thickness;
      }
      ctx.stroke();
    }
    
    // Draw nodes
    for (const node of nodes) {
      ctx.save();
      ctx.beginPath();
      ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
      
      const o = node.opacity;
      
      if (node.hovered) {
        ctx.fillStyle = safeRadialGradient(node.x, node.y, node.radius, '#60a5fa', '#3b82f6');
        ctx.fill();
        ctx.strokeStyle = '#93c5fd';
        ctx.lineWidth = 3;
        ctx.stroke();
      } else if (node.highlighted) {
        ctx.fillStyle = safeRadialGradient(node.x, node.y, node.radius, `rgba(96,165,250,${o})`, `rgba(59,130,246,${o*0.8})`);
        ctx.fill();
        ctx.strokeStyle = `rgba(59,130,246,${o})`;
        ctx.lineWidth = 2;
        ctx.stroke();
      } else {
        ctx.fillStyle = safeRadialGradient(node.x, node.y, node.radius, `rgba(59,130,246,${o*0.7})`, `rgba(30,64,175,${o*0.5})`);
        ctx.fill();
        ctx.strokeStyle = `rgba(59,130,246,${o*0.6})`;
        ctx.lineWidth = 1.5;
        ctx.stroke();
      }
      
      // Label
      const fontSize = Math.max(10, Math.min(14, node.radius * 0.55));
      ctx.font = `${fontSize}px Inter, sans-serif`;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.shadowColor = 'rgba(0, 0, 0, 0.8)';
      ctx.shadowBlur = 4;
      ctx.shadowOffsetX = 0;
      ctx.shadowOffsetY = 1;
      
      if (node.hovered || node.radius > 18) {
        ctx.fillStyle = `rgba(255, 255, 255, ${o})`;
        ctx.fillText(node.id, node.x, node.y);
      }
      ctx.restore();
    }
    
    // Tooltip
    if (hoveredNode && !isDragging) {
      ctx.save();
      const text = `${hoveredNode.id} (${hoveredNode.count} article${hoveredNode.count !== 1 ? 's' : ''})`;
      ctx.font = '13px Inter, sans-serif';
      const metrics = ctx.measureText(text);
      const padding = 10;
      const boxWidth = metrics.width + padding * 2;
      const boxHeight = 28;
      const boxX = clamp(hoveredNode.x - boxWidth / 2, 0, width - boxWidth);
      const boxY = hoveredNode.y - hoveredNode.radius - boxHeight - 12;
      
      ctx.fillStyle = 'rgba(17, 17, 17, 0.95)';
      ctx.strokeStyle = '#3b82f6';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.roundRect(boxX, boxY, boxWidth, boxHeight, 6);
      ctx.fill();
      ctx.stroke();
      
      ctx.fillStyle = '#ffffff';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.shadowColor = 'transparent';
      ctx.fillText(text, boxX + boxWidth / 2, boxY + boxHeight / 2);
      ctx.restore();
    }
  }
  
  let iterations = 0;
  const maxIterations = 400;
  
  function animate() {
    if (iterations < maxIterations || isDragging) {
      simulate();
      iterations++;
    }
    render();
    requestAnimationFrame(animate);
  }
  
  requestAnimationFrame(animate);
  
  // Handle resize
  let resizeTimeout;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(() => {
      const r = container.getBoundingClientRect();
      canvas.width = r.width;
      canvas.height = 500;
      width = canvas.width;
      height = canvas.height;
      iterations = 0;
    }, 250);
  });
});
