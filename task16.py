from operator import gt, lt, eq
from functools import reduce

from utilities import get_file

puzzle_input = get_file('16')

class Packet():
    '''Base for other packet types.'''

    def __init__(self, version, packet_type, data):
        self.packet_version = version 
        self.packet_type = packet_type
        self.raw_data = data
        self.data_length = 0
        self.total_length = 0

    def print_packet(self):
        '''Print data contained in packet.

        If packet is operator packet, it will print all packets it contains.
        '''

        if isinstance(self, LiteralPacket):
            print(self)
        else:
            print(self)
            for p in self.packets:
                p.print_packet()

    @staticmethod
    def get_packet_info(packet):
        '''Check packet type and return it.
        Args:
            packet: packet to check
        Returns:
            Integer.
        '''

        packet_version, packet_type = int(packet[:3], 2), int(packet[3:6], 2)
        return packet_version, packet_type
    
class LiteralPacket(Packet):
    '''Packet that contain literal data.'''

    def __init__(self, version, data):
        super().__init__(version, 4, data)
        self.value = None    
        self.set_data()
        #print('lit:',self.packet_version, self.packet_type, self.data_length, self.raw_data)

    def set_data(self):
        '''Reads literal.
        Args:
            packet: string of bits.
        Returns:
            Integer.
        '''

        first_bit = 1
        group_length = 5
        i = 0
        digits = ''
        
        while first_bit != 0:
            bit_group = self.raw_data[i:i + group_length]
            first_bit = int(bit_group[0])
            digit_bits = bit_group[1:]
            digits += digit_bits
            i += group_length

        self.data_length = i 
        self.total_length = self.data_length + 6 # Include header
        self.value = int(digits, 2)
        
        if self.data_length < len(self.raw_data):
            self.raw_data = self.raw_data[:self.data_length]

    def __str__(self):
        return 'Literal packet\nversion: {0}\nraw_data: {1}\ndata: {2}\nlength: {3}\n'.format(self.packet_version, self.raw_data, self.number, self.data_length)

class OperatorPacket(Packet):
    '''Packet that encapsulates other packets.'''

    operations = {
        0: sum, 
        1: lambda l: reduce(lambda x, y: x * y, l), 
        2: min, 
        3: max, 
        5: gt, 
        6: lt, 
        7: eq
    }

    def __init__(self, version, packet_type, data):
        super().__init__(version, packet_type, data)
        self.packets = []
        self.length_type = None
        self.length_bits = None
        self.value = None
        self.set_length()
        self.read_packets()
    
    def set_length(self):
        '''Set information about length type used in packet and length of data.
        
        Length type '0' means that length is in bits. Length type '1' means that length is number of packets.
        '''

        self.length_type = self.raw_data[0]
        self.length_bits = 15 if self.length_type == '0' else 11
        self.data_length = int(self.raw_data[1:self.length_bits + 1], 2)
        self.total_length = self.length_bits + 1 + 6 # Include header
        self.raw_data = self.raw_data[self.length_bits + 1:] # Cut off length info from packet data.
        #print('op:', self.packet_version, self.packet_type, self.length_type, self.length_bits, self.data_length, self.raw_data)

    def read_packets(self):
        '''Read packets and store them in the list.

        Recursive approach calls contructors for nested packet. Recursion ends with literal packets.
        Args:
            packet: string of bits.
        '''
        
        packet_info_length = 6
        info_start = 0
        data_start = packet_info_length
        
        length_left = self.data_length

        while length_left > 0:
            packet_version, packet_type = Packet.get_packet_info(self.raw_data[info_start:])
            data_to_pass = self.raw_data[data_start:]

            if packet_type == 4:
                new_packet = LiteralPacket(packet_version, data_to_pass)                    
            else:
                new_packet = OperatorPacket(packet_version, packet_type, data_to_pass)

            info_start += new_packet.total_length
            data_start = info_start + packet_info_length

            self.total_length += new_packet.total_length
            self.packets.append(new_packet)
            
            if self.length_type == '0':
                length_left -= new_packet.total_length
            else:
                length_left -= 1
        
        
        values = [x.value for x in self.packets]
        try:
            self.value = self.operations[self.packet_type](values)
        except TypeError:
                self.value = self.operations[self.packet_type](*values)
        
        if isinstance(self.value, bool):
            self.value = int(self.value)


    def __str__(self):
        return 'Operator packet\nversion: {0}\ntype: {1}\ndata: {2}\nlength_type: {3}\nlength: {4}\npackets_length: {5}\n'.format(self.packet_version, self.packet_type, self.raw_data, self.length_type, self.data_length, len(self.packets))

def hex_to_bin(hex_string):
    '''Converts hex string to binary string.
    Args:
        hex_string: string of hex digits.
    Returns:
        String of bits.
    '''

    #Required to keep leading zeroes after conversion.
    leading_zero_numbers = {
    '0' : '0000',
    '1' : '000',
    '2' : '00',
    '3' : '00',
    '4' : '0',
    '5' : '0',
    '6' : '0',
    '7' : '0',
    }
    binary = bin(int(puzzle_input[0:], 16))[2:]
    try:
        if int(hex_string[0]) < 8:
            return leading_zero_numbers[hex_string[0]] + binary
    except ValueError:
        pass
    return binary

def extract_data(binary_data, start_index=6):
    '''Build a packet based on it's type.

    Args:
        packet: binary number as a string
    Returns:
        OperatorPacket or LiteralPacket object.
    '''

    packet_version, packet_type = Packet.get_packet_info(binary_data)
    packet_data = binary_data[start_index:]
    
    if packet_type == 4:
        return LiteralPacket(packet_version, packet_data)
    
    return OperatorPacket(packet_version, packet_type, packet_data)

def sum_versions(packet):
    '''Return sum of all packet versions (including nested packets).
    
    Args:
        packet: packet to check
    Returns:
        Integer.
    '''

    if isinstance(packet, LiteralPacket):
        return packet.packet_version
    else:
        sum = packet.packet_version
        for p in packet.packets:
            sum += sum_versions(p)
        return sum

# Part 1
binary_data = hex_to_bin(puzzle_input)
packet = extract_data(binary_data)
print('Part 1:', sum_versions(packet))

# Part 2
print('Part 2:', packet.value)

