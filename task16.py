from utilities import get_file

puzzle_input = get_file('16')
packet = bin(int(puzzle_input, 16))[2:] # Hex to bin.

class Packet():
    '''Base for other packet types.'''
    packet_version = None

    def __init__(self, version):
        self.packet_version = version 

    @staticmethod
    def get_packet_info(packet):
        '''Checks packet type and returns it.
        Args:
            packet: packet to check
        Returns:
            Integer.
        '''

        packet_version, packet_type = int(packet[:3], 2), int(packet[3:6], 2)
        return packet_version, packet_type
    

class LiteralPacket(Packet):
    '''Packet that contain literal data.'''
    
    raw_data = None
    data = None    
    length = None

    def __init__(self, version, data):
        super().__init__(version)
        self.raw_data = data
        self.read_data()

    def read_data(self):
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

        data_length = i
        
        self.length = data_length
        self.data = int(digits, 2)

        if self.length < len(self.raw_data):
            self.raw_data = self.raw_data[:self.length]

    def __str__(self):
        return 'Literal packet\nversion: {0:2}\nraw_data: {1}\ndata: {2:8}\nlength: {3:4}\n'.format(self.packet_version, self.raw_data, self.data, self.length)

class OperatorPacket(Packet):
    '''Packet that encapsulates other packets.'''
    
    packet_type = None
    raw_data = None
    packets = []
    length_type = None
    length = None

    def __init__(self, version, packet_type, length_type, length, packet):
        super().__init__(version)
        self.packet_type = packet_type
        self.raw_data = packet
        self.length_type = length_type
        self.length = length
    
    def read_packets(self):
        '''Reads packets and store them in the list.

        Args:
            packet: string of bits.
        '''
        
        packet_version, packet_type = get_packet_info(self.raw_data)
        
        if packet_type == 4:
            if self.length_type == 0:
                length_left = self.length
                while length_left > 0:
                    new_packet = LiteralPacket(packet_version, self.raw_data[6:self.length])
                    length
                    #self.packets.append(LiteralPacket(packet_version, new_packet))


            

def extract_data(first_packet):
    '''Extract all data from first packet.

    Args:
        packet: binary number as string
    Returns:
        Packet of given type. Operator packets contain other packets.
    '''

    packet_version, packet_type = get_packet_info(first_packet)
    
    if packet_type == 4:
        packet_data = first_packet[6:]
        return LiteralPacket(packet_version, packet_data)
    else:
        length_type = packet[7]
        length_bits = 15 if length_type == '0' else 11
        length = int(packet[8:8 + length_bits], 2)
        
        return OperatorPacket(packet_version, packet_type, length_type, length, packet[8 + length_bits:])

# Part 1
packet = OperatorPacket(version, packet_type, length_type, length, packet)
print('Part 1:', )
