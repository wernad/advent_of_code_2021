from utilities import get_file

puzzle_input = get_file('16')
packet = bin(int(puzzle_input, 16))[2:] # Hex to bin.

class Packet():
    '''Base for other packet types.'''
    packet_version = None

    def __init__(self, version):
        self.packet_version = version 

    @staticmethod
    def check_packet_type(packet):
        '''Checks packet type and returns it.
        Args:
            packet: packet to check
        Returns:
            Integer.
        '''

        return int(packet[3:6], 2)

class LiteralPacket(Packet):
    '''Packet that contain literal data.'''
    
    raw_data = None
    data = None
    length = None

    def __init__(self, version, data):
        super().__init__(version)
        self.raw_data = data
        self.read_data(data)

    def read_data(self, packet):
        '''Reads literal.
        Args:
            packet: string of bits.
        Returns:
            Integer.
        '''
        first_bit = 1
        i = 0
        numbers = ''
        while first_bit != 0:
            number_part = packet[i:i+5]
            first_bit = int(number_part[0])
            number = number_part[1:]
            numbers += number
            i += 5
        data_length = len(numbers) + len(numbers) % 4
        
        self.length = data_length
        self.data = int(numbers, 2)

    def __str__(self):
        return 'Literal packet\nversion: {0:2}\nraw_data: {1}\ndata: {2:8}\nlength: {3:4}\n'.format(self.packet_version, self.raw_data, self.data, self.length)

def decapsulate_packet(first_packet):
    '''Extract all packets from first packet and return them in dictionary.

    Args:
        packet: binary number as string
    Returns:
        Dictionary of dictionaries. Depth of a packet is a key, dictionary of packet as value. Dictionaries that are nested use packet order as key.
    '''

    packet_dict = {}

    while packet_queue:
        depth, order, read_type, read_count, packet = packet_queue.pop(0)
        
        packet_version = int(packet[:3], 2)
        

        if packet_type == 4:
            data_length, literal = read_literals(packet)
            packet_dict[depth] = {order: (packet_version, packet_type, literal)}

            if data_length < packetpacket[6:6+data_length] == '1'*data_length:
                packet_queue.append((depth+1, order, packet[6+data_length:]))
        elif packet_type != 4:
            length_type = packet[7]
            length = 15 if length_type == '0' else 11

            if length == 15:
                packet_length = int(packet[8:length], 2)

            else:
                packet_count = int(packet[8:length], 2)



    print(packet_dict)

        



# Part 1
packet = LiteralPacket(5, packet[6:])
print('Part 1:', str(packet))
