# Annotations Created by TURBODRIVER

"""
Sim Interrupt Request Interface
"""

def handle_sim_irq(zone_id: 'int') -> 'int':
    """
    handle_sim_irq(zoneid) -> int
    
    Process zero (0) or more interrupt-level tasks waiting. Returns the number processed
    """
