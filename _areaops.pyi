"""
Area Instance Operations Interface
"""


def accept_invitation(invitationId, accepterId):
    """
    Accept the specified invitation.
    """


def cancel_invitation(invitationId, accepterId):
    """
    Cancel the specified invitation.
    """


def load_gsi(arg0) -> "bytes":
    """
    -> bytes
    
    Load the last persisted GSI state as a bytes object
    """


def op_profile_enable(profiling_enabled):
    """
    Turns profiling off or on.
    """


def op_profile_pbenable(message, profiling_enabled):
    """
    When profiling_enabled is True, we are enabling protocol buffer profiling.
    """


def op_profile_pbwrap(message, serialization_prologue):
    """
    When serialization_prologue is True, the message passed by the first argument is about to be serialized.
    """


def op_profile_screen(method, module):
    """
    Only log profile information on a specific method located in an optional module argument
    """


def op_request(opcode, data):
    """
    Request an operation to execute in the Area Instance .
    """


def query_invitations(requesterSessionId):
    """
    Query for invitations sent by or to the requester.
    """


def reject_invitation(invitationId, rejecterId):
    """
    Reject the specified invitation.
    """


def save_gsi(zoneid, gsi_data):
    """
    Persist the given string representation of a GSI dump.
    """


def send_cohab_invitation(inviterSessionId, accepterId, numSlots, householdId):
    """
    Send a cohabitation invitation from the account associated with the inviterSessionId to the account associated with the accepterId, optionally specifying a specific householdId to invite. The invitation will allow for numSlots sims to come over.
    """


def send_relationship_handshake(inviterSessionId, accepterNucleusId, inviterSimId, accepterSimId):
    """
    Send a relationship handshake request from the account associated with the inviterSessionId to the account associated with the accepterId, specifying two sims that are enacting the handshake.
    """


def trigger_assert(*args):
    """
    Trigger an assert.
    """
