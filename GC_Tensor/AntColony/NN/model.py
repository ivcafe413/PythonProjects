import tensorflow as tf

class Model:
    def __init__(self, num_tiles, num_tile_types, num_actions, batch_size):
        # Number of environment tiles in agent's awareness (state X)
        self.num_tiles = num_tiles
        # Number of possible tile types in environment (state Y)
        self.num_tile_types = num_tile_types
        # Number of possible actions by agent
        self.num_actions = num_actions
        # Batch size for training
        self.batch_size = batch_size

        self.define_model()

    def define_model(self):
        # State data, initialized to placeholder
        # TODO: FLATTEN
        self.states = tf.placeholder(shape = [None, self.num_tiles * self.num_tile_types], dtype = tf.float32)
        # Initial Q learning table
        self.q_s_a = tf.placeholder(shape = [None, self.num_actions], dtype = tf.float32)

        # Define hidden layers here
        # Layer 1 taking states as input, 100 nodes, ReLU activation
        hiddenLayer1 = tf.layers.dense(self.states, 100, activation=tf.nn.relu)
        # Layer 2 taking Layer 1 as input, 100 nodes, ReLU activation
        hiddenLayer2 = tf.layers.dense(hiddenLayer1, 100, activation=tf.nn.relu)
        # Output Layer mapping to possible actions, linear activation
        self.logits = tf.layers.dense(hiddenLayer2, self.num_actions)

        loss = tf.losses.mean_squared_error(self.q_s_a, self.logits)

        self.optimizer = tf.train.AdamOptimizer().minimize(loss)
        # self.var_init = tf.global_variables_initializer()

    def predict_one(self, state, sess):
        return sess.run(self.logits, feed_dict={self.states: state.reshape(1, self.num_tiles, self.num_tile_types)})

    def predict_batch(self, states, sess):
        return sess.run(self.logits, feed_dict={self.states: states})

    def train_batch(self, sess, x_batch, y_batch):
        sess.run(self.optimizer, feed_dict={self.states: x_batch, self.q_s_a: y_batch})